from bs4 import BeautifulSoup
from datetime import datetime
import statistics
import requests
import csv
import codecs
from urls import url_dictionary
from urllib.error import HTTPError, URLError


startTime = datetime.now()


def extract_properties(entries_on_page, list_so_far):
    for body in entries_on_page:
        num_of_rows = len(body.find_all('tr'))
        if num_of_rows > 2:
            try:
                price = body.find('div', class_='price').text.strip().split(' ')
                if price[0].isdigit() and price[1].isdigit():
                    price = int(price[0] + price[1])
                    description = body.find_all('tr')[3].text.strip()
                    sq_m = int(description.split(' ')[0])
                    price_per_sqm = price / sq_m
                    region = body.find('a', class_='lnk2')
                    region = region.text.split(', ')[1]
                    if f'{region}' not in list_so_far:
                        list_so_far[f'{region}'] = []
                    list_so_far[f'{region}'].append(int(price_per_sqm))
            except (AttributeError, KeyError) as ex:
                print(ex)
                continue
    return list_so_far


def find_pages(current_page, last_p, soup, real_estates):
    while current_page <= last_p:
        if current_page > 1:
            c_url = baseUrl + str(current_page)
            try:
                body = requests.get(c_url, timeout=5, headers={"Accept-Language": "bg-BG, bg;q=0.5"})
                soup = BeautifulSoup(body.content.decode('windows-1251'), 'lxml')
            except (URLError, HTTPError) as err:
                print(err)
                continue

        props = soup.find('table')
        real_estates = extract_properties(props.find_all('table', attrs={'width': '660'}), real_estates)
        current_page += 1
    return real_estates


f = codecs.open('./properties.csv', 'w', encoding='utf-8-sig')
csv_writer = csv.DictWriter(f, fieldnames=('region', 'num_of_entries', 'avg_p', 'mean_p'), lineterminator='\n')
csv_writer.writeheader()

for url in url_dictionary.values():
    baseUrl = url
    curr_page = 1
    currUrl = baseUrl + str(curr_page)
    properties={}
    try:
        body_text = requests.get(currUrl, timeout=5, headers={"Accept-Language": "bg-BG, bg;q=0.5"})
        soup = BeautifulSoup(body_text.content.decode('windows-1251'), 'lxml')
        last_page = int(soup.find('span', class_='pageNumbersInfo').text.split(' ')[-1])
    except (URLError, HTTPError) as exc:
        print(exc)
        continue

    final_list_results = find_pages(curr_page, last_page, soup, properties)

    for key, value in final_list_results.items():
        csv_writer.writerow({
            'region': key,
            'num_of_entries': len(value),
            'avg_p': str(int(sum(value) / len(value))),
            'mean_p': str(int(statistics.median(value)))
        })


f.close()
print(datetime.now() - startTime)

