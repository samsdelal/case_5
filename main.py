import requests

"""from bs4 import BeautifulSoup as bs



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

"""
# f = open('players.txt', '+')
for i in
    with open("players.txt", "r") as f_pl:
        str = f_pl.readline(limit=22)

        url = 'http://www.nfl.com/player/jimmygaroppolo/2543801/profile'
        response = requests.get(url)

        name_position = str(response.text).find('player-name')
        text = str(response.text)
        name_end = text.find('<', name_position)
        name = str(response.text)[name_position + 13:name_end - 12]


        def text_func(TDS):
            tds_pos = str(response.text).find(TDS)
            text_tds = str(response.text)
            TDS_1 = text_tds.find('player-quick-stat-item-body', tds_pos)
            TDS_2 = text_tds.find('player-quick-stat-item-body', tds_pos)
            print(TDS_2)
            SEND  = text_tds[TDS_1 + 29:TDS_2 + 37].replace('</p', '').replace('>', '').replace(' ', '')
            #print(text_tds[TDS_1 + 29:TDS_2 + 31])
            return SEND

        int_send = text_func('INT')
        tds_send = text_func('TDS')
        yds_send = text_func('YDS')
        rtg_send = text_func('RTG')
        print('---------------')
        print('Name: ', name)
        print('TDS: ', tds_send)
        print('INT: ', int_send)
        print('YDS: ', yds_send)
        print('RTG: ', rtg_send)

