import requests
from bs4 import BeautifulSoup

_PROXIES = {
    "http": "socks5://0.0.0.0:9050",
    "https": "socks5://0.0.0.0:9050",
}


def get_html_text(url: str):
    html = requests.get(url).text
    # html = requests.get(url).text
    print('111')
    soup = BeautifulSoup(html, "html.parser")
    return soup
