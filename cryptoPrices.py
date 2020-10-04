from bs4 import BeautifulSoup
import requests
import sys

def crytpo_prices(search):
    r = requests.get('https://www.coinbase.com/price/' + search)
    div_class = 'Flex-l69ttv-0 AssetChartAmount__Wrapper-sc-1b4douf-0 bIaMsv'
    soup = BeautifulSoup(r.text, 'lxml')

    currency = soup.find_all('div', {'class': div_class})
    for curr in currency:
        currency = curr.text
    print(f'{search} is currently {currency}')

if __name__ == '__main__':
    search = sys.argv[-1]
    if len(sys.argv) > 1:
        crytpo_prices(search)
    else:
        print('Not a crypto or typo. Enter python cryptoPrices.py bitcoin')