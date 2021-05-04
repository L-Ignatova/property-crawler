from datetime import datetime
import statistics
import csv
import codecs
from urls import url_dictionary
from get_soup import get_soup
from get_pages import find_pages
from urllib.error import HTTPError, URLError
from tkinter import *
from tkinter import ttk

startTime = datetime.now()
f = codecs.open('./properties.csv', 'w', encoding='utf-8-sig')
csv_writer = csv.DictWriter(f, fieldnames=('region', 'num_of_entries', 'avg_p', 'mean_p'), lineterminator='\n')
csv_writer.writeheader()


def show_def(districts):
    for url in districts:
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


checkboxes = {}


def show():
    checkbox_values = [checkboxes[obj].get() for obj in checkboxes.keys() if checkboxes[obj].get() != '0']
    root.quit()
    show_def(checkbox_values)


root = Tk()
root.title('Pick your districts')
root.geometry('500x400')

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
scrlbr = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
scrlbr.pack(side=RIGHT, fill=Y)
my_canvas.configure(yscrollcommand=scrlbr.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))
second_frame = Frame(my_canvas)
my_canvas.create_window((0,0), window=second_frame, anchor='nw')


for index, (district, link) in enumerate(url_dictionary.items()):
    var = StringVar()
    c = Checkbutton(second_frame,text=district,variable=var,onvalue=link, offvalue='0',height=1,width=40)
    checkboxes[c] = var
    c.deselect()
    c.pack()

btn = Button(second_frame, text='Get properties', command=show, padx=20, pady=5).pack()
root.mainloop()

f.close()
print(datetime.now() - startTime)