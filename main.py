from datetime import datetime
import statistics
import csv
import codecs
from urls import url_dictionary
from get_soup import get_soup
from get_pages import find_pages
from urllib.error import HTTPError, URLError


startTime = datetime.now()
f = codecs.open('./properties.csv', 'w', encoding='utf-8-sig')
csv_writer = csv.DictWriter(f, fieldnames=('region', 'num_of_entries', 'avg_p', 'mean_p'), lineterminator='\n')
csv_writer.writeheader()

for url in url_dictionary.values():
    baseUrl = url
    curr_page = 1
    currUrl = baseUrl + str(curr_page)
    properties={}
    try:
        soup = get_soup(currUrl)
        last_page = int(soup.find('span', class_='pageNumbersInfo').text.split(' ')[-1])
    except (URLError, HTTPError) as exc:
        print(exc)
        continue

    final_list_results = find_pages(baseUrl, curr_page, last_page, soup, properties)
    for key, value in final_list_results.items():
        csv_writer.writerow({
            'region': key,
            'num_of_entries': len(value),
            'avg_p': str(int(sum(value) / len(value))),
            'mean_p': str(int(statistics.median(value)))
        })


f.close()
print(datetime.now() - startTime)