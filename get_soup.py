from bs4 import BeautifulSoup
import requests


def get_soup(current_url):
    body = requests.get(current_url, timeout=5, headers={"Accept-Language": "bg-BG, bg;q=0.5"})
    return BeautifulSoup(body.content.decode('windows-1251'), 'lxml')
