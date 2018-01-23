from projekt_stadion import *
import csv

def niz_z_vejico_v_niz(niz):
    nov_niz = ''
    for i in niz:
        if i != ',':
            nov_niz += i
        else:
            nov_niz += ''
    return nov_niz

def slovar_stadionov(sez):
    l = []
    for nabor in sez:
        stadion = {}
        for i, j in enumerate(nabor):
            if i == 0:
                stadion['ime'] = j
            if i == 1:
                stadion['kapaciteta'] = int(niz_z_vejico_v_niz(j))
            if i == 2:
                stadion['mesto'] = j
            if i == 3:
                stadion['drzava'] = j
            if i == 4:
                stadion['ekipa'] = j
            if i == 5:
                stadion['uporaba1'] = j
            if i == 6:
                stadion['uporaba2'] = j
            if i == 7:
                stadion['uporaba3'] = j
            if i == 8:
                stadion['uporaba4'] = j
        l.append(stadion)
    return l

def zapisi_tabelo(slovarji, imena_polj, ime_datoteke):
     with open(ime_datoteke, 'w', encoding='utf-8') as csv_dat:
         writer = csv.DictWriter(csv_dat, fieldnames=imena_polj)
         writer.writeheader()
         for slovar in slovarji:
             writer.writerow(slovar)

polja = ['ime', 'kapaciteta', 'mesto', 'drzava', 'ekipa', 'uporaba1', 'uporaba2', 'uporaba3', 'uporaba4']
#shrani = shrani_html()
preberi = preberi_dat_v_niz(stadioni_mapa, html_datoteka)
#print(preberi)
sez = seznam_nizov_oblike_rx(preberi)
#print(sez)
seznam = (seznam_stadionov(sez))
seznam_naborov = razclenjeni_stadioni(seznam)
zapisi_csv = zapisi_tabelo(slovar_stadionov(seznam_naborov), polja, csv_datoteka)
print(len(seznam_naborov))
#print(seznam_naborov)