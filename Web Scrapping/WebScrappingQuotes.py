# Grabbing the unique authors from the website

import requests, bs4

base_url = 'http://quotes.toscrape.com/page/'
authors = set()
page_still_valid = True
page = 1

while page_still_valid:

    page_url = base_url + str(page)
    response = requests.get(page_url)

    if 'No quotes found!' in response.text:
        break

    soup = bs4.BeautifulSoup(response.text, 'lxml')

    for name in soup.select('.author'):
        authors.add(name.text)

    page += 1

print(authors, sep='\n')