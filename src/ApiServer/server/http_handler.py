# FIXME: handler별로 파일 분리

import logging
from http import HTTPStatus
import base64
from aiohttp import web

from ..server.config import Config
from ..Caller.caller import Caller
import requests
from bs4 import BeautifulSoup
import json
import os
import asyncio
from aiohttp_prometheus_exporter.handler import metrics


def get_html_text(url: str):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    return soup


def get_base_wz(config) -> dict:
    cwd = os.path.dirname(os.path.realpath(__file__))
    base_wz_code_path = os.path.join(cwd, 'data', 'test_base_wz.json')
    if base_wz_code_path:
        if os.path.isfile(base_wz_code_path):
            with open(base_wz_code_path) as f:
                base_wz = json.load(f)
                return base_wz

    wcr_server_host = config.wcr_server_host
    wcr_server_port = config.wcr_server_port
    wcr_server_protocol = config.wcr_server_protocol

    url = f"{wcr_server_protocol}://{wcr_server_host}:{wcr_server_port}/code"

    res = requests.get(url, verify=False)
    base_wz = json.loads(res.text)

    if base_wz_code_path:
        with open(base_wz_code_path, "w") as f:
            json.dump(base_wz, f, ensure_ascii=False, indent="\t")

    return base_wz

# TODO : url argparser로 받기


def get_avatar_item_encoding_string(item_code: dict, ) -> dict:
    get_avatar_server_url = "http://localhost:8080/avatar_image"
    encoding_images = {}

    # TODO : 개별 아바타 얻는 부분 추가, Wz 서버 icon으로 표시 업데이트 후 추가 예정
    '''
    obj = {}

    for key, value in item_code.items():
        if key == 'skin':
            key = 'head'
        if key == 'shield':
            continue
        if value == '0':
            continue
        if key == 'name':
            continue
        obj[key] = value

    obj['bs'] = 'true'

    for key, value in obj.items():
        if key == 'bs':
            continue
        res = requests.post(avatar_server_item_url, json={'avatar': {key: value}})

        encoding_images[key] = res.text
    '''

    res = requests.post(get_avatar_server_url, json={"avatar": item_code})
    encoding_images['avatar'] = res.text
    return encoding_images


def get_item_code_name(base_wz: dict , item_code: dict) -> dict:
    item_code_name = {}
    for key , value in item_code.items():
        if value == '0':
            continue
        if key == 'hair':
            value = value.split('+')[0]
            item_code_name[key] = base_wz[key][value]['name']
            continue
        if key == 'skin':
            key = 'head'
            item_code_name[key] = base_wz[key][item_code['skin']]['name']
            continue
        if key == 'shield':
            continue
        item_code_name[key] = base_wz[key][item_code[key]]['name']
    return item_code_name


class HttpHandler:
    def __init__(
        self,
        logger: logging.Logger,
        config: Config,
        avatar_caller: Caller = None,
        inference_caller: Caller = None,
    ):
        self.logger = logger
        self.config = config
        self.avatar_caller = avatar_caller if avatar_caller is not None else Caller(
            logger=logger,
            server_host=config.avatar_server_host,
            server_protocol=config.avatar_server_protocol,
            server_port=config.avatar_server_port,
            retry_num=config.avatar_caller_retry_num,
            timeout=config.avatar_caller_timeout,
            backoff=config.avatar_caller_backoff,
        )
        self.inference_caller = inference_caller if inference_caller is not None else Caller(
            logger=logger,
            server_host=config.inference_server_host,
            server_protocol=config.inference_server_protocol,
            server_port=config.inference_server_port,
            retry_num=config.inference_caller_retry_num,
            timeout=config.inference_caller_timeout,
            backoff=config.inference_caller_backoff,
        )

    def get_routes(self):
        return [
            web.get("/", self.index_handler),
            web.get("/healthcheck", self.healthcheck_handler),
            web.post('/character_code_web_handler', self.character_code_web_handler),
            web.post('/infer_code_web_handler', self.infer_code_web_handler),
            web.post('/v1/recommend-cody', self.recommend_handler),
            web.post('/v1/character-info', self.character_info_handler),
            web.get('/metrics',metrics())
        ]

    async def index_handler(self, request: web.Request):
        """ """
        return web.Response(body="-", status=HTTPStatus.OK)

    async def healthcheck_handler(self, request: web.Request):
        """ """
        return web.Response(body="200 OK", status=HTTPStatus.OK)

    async def character_code_web_handler(self, request: web.Request) -> web.Response:
        avatar_server_url = "http://localhost:8080/packed_character_look"

        post = await request.text()
        post = json.loads(post)
        self.logger.info(f"web server character request information: {post}")
        res = post['name']

        maple_gg_url = f'https://maple.gg/u/{res}'

        soup = get_html_text(maple_gg_url)
        img_tag = soup.find_all(class_="character-image")[1]["src"]
        self.logger.info(f"crawling character url : {img_tag}")

        encrypted_code = img_tag.replace('https://avatar.maplestory.nexon.com/Character/', '').replace('.png', '')
        response = requests.post(avatar_server_url, json={"packed_character_look": encrypted_code})
        self.logger.info(f"web server character code response: {response.text}")
        return web.json_response({"character_code" : response.text})
#       return web.Response(body=response.text, status=HTTPStatus.OK)

    async def infer_code_web_handler(self, request: web.Request) -> web.json_response:
        result_inference = {}

        post = await request.text()
        post = json.loads(post)
        post = post["character_code_result"]
        self.logger.info(f"inference request text : {post}")

        # response = requests.post("http://localhost:8080/inference", post)  -> infer 서버에 사용자의 코드 요청
        # 추천된 코드를 json으로 저장하여 response로 받는다고 가정

        response_infer_code = '{"face": "54002", "cap": "1005041", "longcoat": "1053240", "weapon": "1703048", "cape": "1103332", "coat": "0", "glove": "1082703", "hair": "61481+3*50", "pants": "0", "shield": "1092067", "shoes": "1073534", "faceAccessory": "1012050", "eyeAccessory": "1022079", "earrings": "1032022", "skin": "12024"}'  # noqa: E501
        response_infer_code = json.loads(response_infer_code)
        self.logger.debug(f"inference character code : {response_infer_code}")
        encoding_images_string = get_avatar_item_encoding_string(item_code=response_infer_code)
        self.logger.info(f"avatar and item base64 encoding string : {encoding_images_string}")
        base_wz = get_base_wz(self.config)
        self.logger.info(f"base_wz_code keys: {base_wz.keys()}")

        item_code_name = get_item_code_name(base_wz=base_wz, item_code=response_infer_code)
        self.logger.info(f"inference item_code_name : {item_code_name}")

        result_inference['encoding_image_string'] = encoding_images_string
        result_inference['infer_item_code_name'] = item_code_name

        return web.json_response(result_inference)

    async def recommend_handler(self, request: web.Request):
        post = await request.json()
        print("post : ",post)
        encrypted_character_uri = post["crypto_uri"]
        parts_to_change = post["parts"]

        character_data = await self.avatar_caller.request(
            route_path="/character_look_data",
            packed_character_look=encrypted_character_uri,
        )
        result = {}
        gender = character_data["gender"]

        for part_image in character_data:
            if "_image" in part_image:
                part = part_image[:-6]
                result[part] = character_data[part]

        part_image_to_change = [
            character_data[f"{part}_image"] for part in parts_to_change
        ]

        changed_parts = [
            await self.inference_caller.request(
                route_path=f"/v1/models/complement-model-{gender}-{part}:predict",
                instances=part_image_to_change,
            )
            for part in parts_to_change
        ]

        for part, response_obj in zip(parts_to_change, changed_parts):
            predictions = response_obj["predictions"]
            for prediction_prob, prediction_item in predictions[0]:
                if part == "hair":
                    mix_part = character_data[part].split('+')
                    prediction_item += mix_part[0][-1]
                    if len(mix_part) == 2:
                        prediction_item += '+' + mix_part[1]
                elif part == "face":
                    prediction_item = prediction_item[:-2] + character_data[part][-3] + prediction_item[-2:]
                result[part] = prediction_item
                if character_data[part] != prediction_item:
                    break
        recommend_image = await self.avatar_caller.request(
            route_path="/avatar_image",
            avatar=result,
        )
        print("recommend_handler: 200 OK")
        return web.json_response({
            "recommended image": recommend_image,
            "result_parts": await self._get_avatar_info(result),
        })

    def get_html_text(self, url: str):
        # TODO: change to async
        html = requests.get(url).text
        # html = requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")
        return soup

    def _get_image_url_list_from_maplegg(self, nickname: str):
        # TODO: change to async
        """user_info에 대해 maplegg로 부터 image_url_list를 받아오는 메소드"""
        url = "https://maple.gg/u/{}".format(nickname)
        soup = self.get_html_text(url)
        img_tag = soup.find_all(class_="character-image")[1:-1]
        return [tag["src"] for tag in img_tag][0]

    def get_as_base64(self, url: str):
        # TODO: change to async
        return base64.b64encode(requests.get(url).content).decode(encoding='utf-8')

    async def _get_avatar_info(self, avatar: dict) -> dict:
        result = {}
        keys = []
        coroutines = []

        keys.append("hair_thum")
        coroutines.append(
            self.avatar_caller.request(
                route_path="/hair_image",
                hair=avatar["hair"],
            )
        )

        keys.append("hair_name")
        coroutines.append(
            self.avatar_caller.request(
                route_path="/item_name",
                code=avatar["hair"],
            )
        )

        keys.append("eye_thum")
        coroutines.append(
            self.avatar_caller.request(
                route_path="/eye_image",
                eye=avatar["face"],
            )
        )

        keys.append("eye_name")
        coroutines.append(
            self.avatar_caller.request(
                route_path="/item_name",
                code=avatar["face"],
            )
        )

        keys.append("weapon_thum")
        coroutines.append(
            self.avatar_caller.request(
                route_path="/icon",
                icon=avatar["weapon"],
            )
        )

        keys.append("weapon_name")
        coroutines.append(
            self.avatar_caller.request(
                route_path="/item_name",
                code=avatar["weapon"],
            )
        )

        keys.append("cap_thum")
        coroutines.append(
            self.avatar_caller.request(
                route_path="/icon",
                icon=avatar["cap"],
            )
        )

        keys.append("cap_name")
        coroutines.append(
            self.avatar_caller.request(
                route_path="/item_name",
                code=avatar["cap"],
            )
        )

        keys.append("face_acc_thum")
        coroutines.append(
            self.avatar_caller.request(
                route_path="/icon",
                icon=avatar["faceAccessory"],
            )
        )

        keys.append("face_acc_name")
        coroutines.append(
            self.avatar_caller.request(
                route_path="/item_name",
                code=avatar["faceAccessory"],
            )
        )

        keys.append("eye_acc_thum")
        coroutines.append(
            self.avatar_caller.request(
                route_path="/icon",
                icon=avatar["eyeAccessory"],
            )
        )

        keys.append("eye_acc_name")
        coroutines.append(
            self.avatar_caller.request(
                route_path="/item_name",
                code=avatar["eyeAccessory"],
            )
        )

        keys.append("long_coat_thum")
        coroutines.append(
            self.avatar_caller.request(
                route_path="/icon",
                icon=avatar["longcoat"],
            )
        )

        keys.append("long_coat_name")
        coroutines.append(
            self.avatar_caller.request(
                route_path="/item_name",
                code=avatar["longcoat"],
            )
        )

        keys.append("shoes_thum")
        coroutines.append(
            self.avatar_caller.request(
                route_path="/icon",
                icon=avatar["shoes"],
            )
        )

        keys.append("shoes_name")
        coroutines.append(
            self.avatar_caller.request(
                route_path="/item_name",
                code=avatar["shoes"],
            )
        )

        keys.append("earrings_thum")
        coroutines.append(
            self.avatar_caller.request(
                route_path="/icon",
                icon=avatar["earrings"],
            )
        )

        keys.append("earrings_name")
        coroutines.append(
            self.avatar_caller.request(
                route_path="/item_name",
                code=avatar["earrings"],
            )
        )

        keys.append("glove_thum")
        coroutines.append(
            self.avatar_caller.request(
                route_path="/icon",
                icon=avatar["glove"],
            )
        )

        keys.append("glove_name")
        coroutines.append(
            self.avatar_caller.request(
                route_path="/item_name",
                code=avatar["glove"],
            )
        )

        keys.append("cape_thum")
        coroutines.append(
            self.avatar_caller.request(
                route_path="/icon",
                icon=avatar["cape"],
            )
        )

        keys.append("cape_name")
        coroutines.append(
            self.avatar_caller.request(
                route_path="/item_name",
                code=avatar["cape"],
            )
        )

        thumbnails = await asyncio.gather(*coroutines)
        for part, code in avatar.items():
            result[part] = code
        for key, thumbnail in zip(keys, thumbnails):
            result[key] = thumbnail

        return result

    async def character_info_handler(self, request: web.Request):
        post = await request.json()
        user_name = post["user_name"]
        result = {}
        result["user_name"] = user_name

        image_url = self._get_image_url_list_from_maplegg(user_name)  # TODO: 크롤링해서 이미지 url 받아오는 코드 추가
        result["crt_image"] = self.get_as_base64(image_url)  # TODO: 크롤링해서 이미지 받아오는 코드 추가
        crypto_uri = image_url.replace(
            'https://avatar.maplestory.nexon.com/Character/', ''
        ).replace('.png', '')

        result["crypto_uri"] = crypto_uri
        avatar = await self.avatar_caller.request(
            route_path="/packed_character_look",
            packed_character_look=crypto_uri,
        )

        avatar_result = await self._get_avatar_info(avatar)

        for category, value in avatar_result.items():
            result[category] = value
        
        print("character_info_handler: 200 OK")
        return web.json_response(result)
