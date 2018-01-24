import requests
import re
import os

# url stadiona
stadioni_url = 'https://en.wikipedia.org/wiki/List_of_stadiums_by_capacity'
# mapa v katero se shrani html datoteka
stadioni_mapa = 'stadioni'
# datoteka, v katero se shrani html stran
html_datoteka = 'stadioni.html'
# datoteka, v katero se shrani csv
csv_datoteka = 'stadioni.csv'

def shrani_url_v_niz(url):
    '''spremeni url stran v niz'''
    try:
        r = requests.get(url)
    except:
        # Sproži izjemo, če ne more pridobiti url
        print('napaka pri nalaganju url' + url)
        return None
    return r.text

def pridobi_url(url):
    '''Poskuša pridobiti url naslov.'''
    try:
        r = requests.get(url)
    except:
        # Sproži izjemo, če ne more pridobiti url
        print('napaka pri nalaganju url' + url)
        return None
    return r

def shrani_niz_v_datoteko(text, mapa, datoteka):
    '''Shrani niz od url-ja v datoteko.'''
    os.makedirs(mapa, exist_ok=True)
    pot = os.path.join(mapa, datoteka)
    with open(pot, 'w', encoding='utf-8') as dat:
        dat.write(text)
    return None

def shrani_html():
    '''Shrani niz od url-ja v datoteko html.'''
    text = shrani_url_v_niz(stadioni_url)
    shrani_niz_v_datoteko(text, stadioni_mapa, html_datoteka)

def preberi_dat_v_niz(mapa, datoteka):
    '''Prebere datoteko.'''
    pot = os.path.join(mapa, datoteka)
    with open(pot, 'r', encoding='utf-8') as dat:
        return dat.read()

def seznam_nizov_oblike_rx(stran):
    '''Iz datoteke izlušči izraze oblike <tr>...</tr> in vrne niz izrazov.'''
    rx = re.compile(r'<tr>'
                    r'.+?'
                    r'</tr>'
                    ,
                    re.DOTALL)
    seznam = re.findall(rx, stran)
    return seznam

def seznam_stadionov(sez):
    '''Dobimo seznam in iz njega izluščimo samo tiste, ki vsebujejo podatke stadionov.'''
    new_list = []
    num = 0
    for i in sez:
        if num != 0:
            new_list.append(i)
        else:
            num += 1
    return new_list

def razclenjeni_stadioni(sez):
    '''Damo seznam nizov in funkcija izlušči podatke stadiona v nabor in vrne seznam naborov.'''
    new_list = []
    rx = re.compile(# ime stadiona
                    r'<td><a href="/wiki/.*?" title="(?P<ime>.*?)">.*?</a>.*?</td>'
                    r'.+?'
                    # kapaciteta stadiona
                    r'<td>(?P<kapaciteta>\d{2,3},\d\d\d).*?</td>'
                    r'.+?'
                    # mesto v katerem je stadion
                    r'<td>(<a href=".*?" title=".+?">)?(?P<mesto>.*?)(</a>.*?)?</td>'
                    r'.+?'
                    # drzava v katerem je stadion
                    r'<td>(<.*?>)?(?P<drzava>.*?)(</.*?>)?</td>'
                    r'.+?'
                    r'<td>(<.*?>)?'
                    # ekipa, ki igra na stadionu
                    r'(?P<ekipa>.*?)(<.*?>.*?)?'
                    r'</td>'
                    r'.+?'
                    r'<td>'
                    # uporaba stadiona
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
            # print(y)
            new_list.append((y[0], y[1], y[3], y[6], y[9], y[12], y[21], y[25]))
    return new_list

