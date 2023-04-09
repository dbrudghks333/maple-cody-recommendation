
import json
import os
import requests
import gc

cwd = os.getcwd()
file_path = os.path.abspath(os.path.join(cwd, os.pardir))
file_path = os.path.abspath(os.path.join(file_path, os.pardir))
file_path = os.path.join(file_path, 'mnt/data')

path1 = os.path.join(file_path, 'new_json_data_3001_10000.json')

paths = [path1]
json_datas = []

for path in paths:
    with open(path) as file:
        json_datas.append(json.load(file))

cnt = 60
result = {}
run_from = 59
for json_data in json_datas:
    for data in json_data['data']:
        result[data["nickname"]] = []
        print('!!!!')
        if cnt >= run_from:
            for code_list in data["recent_cody_list"]:
                print(data)
                while True:
                    encrypted_code = code_list.replace(
                        'https://avatar.maplestory.nexon.com/Character/', ''
                    ).replace('.png', '')
                    response = requests.post("http://localhost:8080/character_look_data", json={
                        "packed_character_look": encrypted_code
                    })
                    if response.status_code == 200:
                        result[data["nickname"]].append(json.loads(response.text))
                        print(data["nickname"])
                        
                        break
                    elif response.status_code == 400:
                        break
                    else:
                        print(response.status_code, response.text)

        if len(result) == 100:
            save_path = os.path.join(file_path, f'json_data_result.json')

            if cnt >= run_from:
                with open(save_path, "w") as f:
                    json.dump(result, f, ensure_ascii=False, indent="\t")

            cnt += 1
            del result
            gc.collect()
            result = {}

if len(result) > 0:
    save_path = os.path.join(file_path, f'json_data_result.json')

    cnt += 1

    with open(save_path, "w") as f:
        json.dump(result, f, ensure_ascii=False, indent="\t")

