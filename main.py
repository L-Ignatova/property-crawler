from bs4 import BeautifulSoup
from datetime import datetime
import statistics
import requests
import csv
import codecs
from urls import url_dictionary


startTime = datetime.now()


def extract_properties(bodiesOnPage, list_so_far):
    for body in bodiesOnPage:
        num_of_rows = len(body.find_all('tr'))
        if num_of_rows > 2:
            price = body.find('div', class_='price').text.strip().split(' ')
            if price[0].isdigit() and price[1].isdigit():
                price = int(price[0] + price[1])
                test = body.find_all('tr')[3].text.strip()
                sq_m = int(test.split(' ')[0])
                price_per_sqm = price / sq_m
                region = body.find('a', class_='lnk2')
                region = region.text.split(', ')[1]
                if f'{region}' not in list_so_far:
                    list_so_far[f'{region}'] = []
                list_so_far[f'{region}'].append(int(price_per_sqm))
    return list_so_far


def find_pages(current_page, last_p, soup, real_estates):
    while current_page <= last_p:
        if current_page > 1:
            c_url = baseUrl + str(current_page)
            body = requests.get(c_url, timeout=5, headers={"Accept-Language": "bg-BG, bg;q=0.5"})
            soup = BeautifulSoup(body.content.decode('windows-1251'), 'lxml')
        props = soup.find('table')
        real_estates = extract_properties(props.find_all('table', attrs={'width': '660'}), real_estates)
        current_page += 1
    return real_estates

for url in url_dictionary.values():
    baseUrl = url

    #baseUrl = 'https://www.imot.bg/pcgi/imot.cgi?act=3&slink=6mbmpd&f1='
    curr_page = 1
    currUrl = baseUrl + str(curr_page)
    body_text = requests.get(currUrl, timeout=5, headers={"Accept-Language": "bg-BG, bg;q=0.5"})
    properties={}
    if body_text.status_code == 200:
        soup = BeautifulSoup(body_text.content.decode('windows-1251'), 'lxml')
        last_page = int(
            soup.find('span', class_='pageNumbersInfo')
                .text
                .split(' ')[-1]
        )
        final_list_results = find_pages(curr_page, last_page, soup, properties)
        with codecs.open('./properties.csv', 'w', encoding='utf-8-sig') as f:
            csv_writer = csv.DictWriter(f, fieldnames=('region', 'num_of_entries', 'avg_p', 'mean_p'), lineterminator='\n')
            csv_writer.writeheader()
            for key, value in final_list_results.items():
                csv_writer.writerow({
                    'region': key,
                    'num_of_entries': len(value),
                    'avg_p': str(int(sum(value) / len(value))),
                    'mean_p': str(int(statistics.median(value)))
                })
    else:
        print('404 error')

print(datetime.now() - startTime)

