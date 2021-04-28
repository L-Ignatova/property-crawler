from single_page import extract_properties
from urllib.error import HTTPError, URLError
from get_soup import get_soup


def find_pages(base_url, current_page, last_p, soup, real_estates):
    while current_page <= last_p:
        if current_page > 1:
            c_url = base_url + str(current_page)
            try:
                soup = get_soup(c_url)
            except (URLError, HTTPError) as err:
                print(err)
                continue
        props = soup.find('table')
        real_estates = extract_properties(props.find_all('table', attrs={'width': '660'}), real_estates)
        current_page += 1
    return real_estates


