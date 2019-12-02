import requests
from bs4 import BeautifulSoup as bs



url = requests.get('http://www.nfl.com/player/jimmygaroppolo/2543801/profile')
site = bs(url.content, 'html.parser')

for s in site.select('.player-info'):
    name = s.select('.player-name')
    num = s.select('.player-number')
    print('Name: ',name[0].text)
    print('Number: ', num[0].text)


for i in site.select('.player-quick-stat-item '):
    tds = i.select('.player-quick-stat-item-header')
    res = i.select('.player-quick-stat-item-body')
    print(tds[0].text+':', res[0].text)


