# Web crawler 
## for real estate prices in Sofia districts

Calculates average and mean property prices for Sofia districts (and shows the number of listed entries in each) in popular Bulgarian real estate website imot.bg

Currently the baseUrl is just a sample from the website. The website generates only up to 1,000 entries from chosen parameters so more url's to iterate through are needed for a bigger sample size for each district.

### Languages
Python 3.7

### Libraries
BeautifulSoup, Tkinter (to be used for GUI)

### Challenges
Decoding cyrillic. Website's charset: 'windows-1251'. Resource that helped in the end can be found [here](https://overcoder.net/q/1334854/%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C-html-%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BD%D1%82-%D0%B2-%D0%BA%D0%BE%D0%B4%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B5-utf8).

## ToDo list
- [ ] GUI checklist for choosing districts of interest
- [ ] error handling
