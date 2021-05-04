# Web crawler 
## for real estate prices in Sofia districts

Calculates average and mean property prices (w/ 2 & 3 rooms) for Sofia districts in popular Bulgarian real estate website imot.bg. Also shows the number of entries for each district.

Currently, the program iterates through the urls associated with about half of the districts from the website. The website generates only up to 1,000 entries from chosen parameters so the url corresponding to each district is needed for a bigger sample size.

### Languages
Python 3.7

### Libraries
BeautifulSoup, Tkinter (to be used for GUI)

### Challenges
Decoding cyrillic. Website's charset: 'windows-1251'. Resource that helped in the end can be found [here](https://overcoder.net/q/1334854/%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C-html-%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BD%D1%82-%D0%B2-%D0%BA%D0%BE%D0%B4%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B5-utf8).

## ToDo list
- [x] GUI checklist for choosing districts of interest
- [x] make 'all' checklist option
- [x] error handling
