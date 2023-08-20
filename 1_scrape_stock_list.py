import requests
from bs4 import BeautifulSoup

class sp500_soup:
    def __init__(self):
        self.sp500_dict = {}

    def table_soup(self):
        url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
        response = requests.get(url)
        page_content = response.content
        soup = BeautifulSoup(page_content, 'html.parser')
        self.table = soup.find('table')

    def access_table_data(self):
        self.table_soup()
        rows = self.table.find_all('tr')[1:]
        for row in rows:
            ticker = row.find_all('td')[0].text.strip()
            company = row.find_all('td')[1].text
            industry = row.find_all('td')[2].text
            location = row.find_all('td')[4].text
            self.sp500_dict[ticker] = company, industry, location
        return self.sp500_dict

sp500 = sp500_soup()

sp500_dict = sp500.access_table_data()

print(sp500_dict)