import requests
import re
import os

stadioni_url = 'https://en.wikipedia.org/wiki/List_of_stadiums_by_capacity'
stadioni_mapa = 'stadioni'
html_datoteka = 'stadioni.html'
csv_datoteka = 'stadioni.csv'
json_datoteka = 'stadioni.json'

def shrani_url_v_niz(url):
    try:
        r = requests.get(url)
    except:
        print('napaka pri nalaganju url' + url)
        return None
    return r.text

def pridobi_url(url):
    try:
        r = requests.get(url)
    except:
        print('napaka pri nalaganju url' + url)
        return None
    return r

def shrani_niz_v_datoteko(text, mapa, datoteka):
    os.makedirs(mapa, exist_ok=True)
    pot = os.path.join(mapa, datoteka)
    with open(pot, 'w', encoding='utf-8') as dat:
        dat.write(text)
    return None

def shrani_html():
    text = shrani_url_v_niz(stadioni_url)
    shrani_niz_v_datoteko(text, stadioni_mapa, html_datoteka)

def preberi_dat_v_niz(mapa, datoteka):
    pot = os.path.join(mapa, datoteka)
    with open(pot, 'r', encoding='utf-8') as dat:
        return dat.read()

def seznam_nizov_oblike_rx(stran):
    rx = re.compile(r'<tr>'
                    r'.+?'
                    r'</tr>'
                    ,
                    re.DOTALL)
    seznam = re.findall(rx, stran)
    return seznam

def seznam_stadionov(sez):
    new_list = []
    num = 0
    for i in sez:
        if num != 0:
            new_list.append(i)
        else:
            num += 1
    return new_list

def razclenjeni_stadioni(sez):
    new_list = []
    rx = re.compile(r'<td><a href="/wiki/.*?" title="(?P<ime>.*?)">.*?</a>.*?</td>'
                    r'.+?'
                    r'<td>(?P<kapaciteta>\d{2,3},\d\d\d).*?</td>'
                    r'.+?'
                    r'<td>(<a href=".*?" title=".+?">)?(?P<mesto>.*?)(</a>.*?)?</td>'
                    r'.+?'
                    r'<td>(<.*?>)?(?P<drzava>.*?)(</.*?>)?</td>'
                    r'.+?'
                    r'<td>(<.*?>)?'
                    r'(?P<ekipa>.*?)(<.*?>.*?)?'
                    r'</td>'
                    r'.+?'
                    r'<td>'
                    r'(<a .*?>)?(?P<uporaba1>.*?)(</a>)?'
                    r'(,? (and)? (<a .*?>)?(?P<uporaba2>.*?)(</a>)?)?'
                    r'(, (<a .*?>)?(?P<uporaba3>.*?)(</a>)?)?'
                    r'(, (<a .*?>)?(?P<uporaba4>.*?)(</a>)?.?)?'
                    r'(((, (<a .*?>)?(?P<uporaba5>.+?)(</a>)?)?))'
                    r'</td>'
                    , re.DOTALL
                    )
    for i in sez:
        nabor = re.findall(rx, i)
        dolzina = 0
        for y in nabor:
            dolzina += len(y)
        # print(dolzina)
        for y in nabor:
            #print(y)
            new_list.append((y[0], y[1], y[3], y[6], y[9], y[12], y[21], y[25]))
    return new_list

