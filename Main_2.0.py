#Boris Kuznecov 50% Odoevcev Sergey 50% Makarov Artem 40$

import urllib.request as ur
with open('players.txt', 'r') as play, open('outputs.txt', 'w') as outp:
    line = play.readlines()
    for i in range(len(line)):
        url = line[i]


        f = ur.urlopen(url)
        s = f.read()
        text = str(s)
        part_name = text.find('TOTAL')

        name = text[text.find('>', part_name) + 1:text.find('</tr>', part_name)]
        name = name.replace('n', '')
        name = name.replace('t', '')
        name = name.replace('d', '')
        name = name.replace('<', '')
        name = name.replace('>', '')
        name = name.replace('/', ' ')
        name = name.replace('\\', '')
        name = name.replace(',', '')
        name = name.split()

        COMP = name[0]
        ATT = name[1]
        YDS = name[3]
        TD = name[5]
        INT = name[6]
        print(COMP, ATT, YDS, TD, INT,file = outp)
