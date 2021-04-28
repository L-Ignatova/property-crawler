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
