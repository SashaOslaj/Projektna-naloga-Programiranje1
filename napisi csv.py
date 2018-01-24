from projekt_stadion import *
import csv

slovar_kontinentov ={
    'Europe': ['Albania', 'Andorra', 'Armenia', 'Austria', 'Azerbaijan',
               'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria',
               'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia',
               'Finland', 'France', 'Georgia', 'Germany', 'Greece','Hungary',
               'Iceland', 'Ireland', 'Italy', 'Kazakhstan', 'Kosovo', 'Latvia',
               'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia',
               'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'Norway',
               'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino', 'Serbia',
               'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey',
               'Ukraine', 'United Kingdom', 'Vatican City'
    ],
    'Asia': ['Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan',
             'Brunei', 'Cambodia', 'China', 'Cyprus', 'Georgia','India', 'Indonesia',
             'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan',
             'Laos', 'Lebanon', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar', 'Burma', 'Nepal',
             'North Korea', 'Oman', 'Pakistan', 'Palestine', 'Philippines', 'Qatar', 'Russia',
             'Saudi Arabia', 'Singapore', 'South Korea', 'Sri Lanka', 'Syria', 'Taiwan', 'Tajikistan',
             'Thailand', 'Timor-Leste', 'Turkey', 'Turkmenistan', 'United Arab Emirates',
             'Uzbekistan', 'Vietnam', 'Yemen'
    ],
    'Africa': ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde',
               'Cameroon', 'Central African Republic', 'Chad', 'Comoros', 'Democratic Republic of the Congo',
               'Republic of the Congo', 'Cote d Ivoire', 'Djibouti', 'Egypt', 'Equatorial Guinea', 'Eritrea',
               'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia',
               'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia',
               'Niger', 'Nigeria', 'Rwanda', 'Sao Tome and Principe', 'Senegal', 'Seychelles', 'Sierra Leone',
               'Somalia', 'South Africa','South Sudan', 'Sudan', 'Swaziland','Tanzania', 'Togo', 'Tunisia', 'Uganda',
               'Zambia', 'Zimbabwe'
    ],
    'North America': ['Antigua and Barbuda', 'Bahamas', 'Barbados', 'Belize', 'Canada', 'Costa Rica', 'Cuba',
                     'Dominica', 'Dominican Republic', 'El Salvador', 'Grenada', 'Guatemala', 'Haiti',
                     'Honduras', 'Jamaica', 'Mexico', 'Nicaragua', 'Panama', 'Saint Kitts and Nevis',
                     'Saint Lucia', 'Saint Vincent and the Grenadines', 'Trinidad and Tobago', 'United States'
    ],
    'South America': ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana',
                      'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela'
    ],
    'Australia and Oceania': ['Australia', 'Fiji', 'Kiribati', 'Marshall Islands', 'Micronesia', 'Nauru',
                              'New Zealand', 'Palau', 'Papua New Guinea', 'Samoa', 'Solomon Islands',
                              'Tonga', 'Tuvalu', 'Vanuatu'
    ]
}

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
        l.append(stadion)
    return l

def dodaj_kontinente(stadioni, kontinenti):
    for stadion in stadioni:
        if stadion['drzava'] in kontinenti['Europe']:
            stadion['kontinent'] = 'Europe'
        if stadion['drzava'] in kontinenti['Asia']:
            stadion['kontinent'] = 'Asia'
        if stadion['drzava'] in kontinenti['Africa']:
            stadion['kontinent'] = 'Africa'
        if stadion['drzava'] in kontinenti['North America']:
            stadion['kontinent'] = 'North America'
        if stadion['drzava'] in kontinenti['South America']:
            stadion['kontinent'] = 'South America'
        if stadion['drzava'] in kontinenti['Australia and Oceania']:
            stadion['kontinent'] = 'Australia and Oceania'
    return stadioni


def zapisi_tabelo(slovarji, imena_polj, ime_datoteke):
     with open(ime_datoteke, 'w', encoding='utf-8') as csv_dat:
         writer = csv.DictWriter(csv_dat, fieldnames=imena_polj)
         writer.writeheader()
         for slovar in slovarji:
             writer.writerow(slovar)

polja = ['ime', 'kapaciteta', 'mesto', 'drzava', 'ekipa', 'uporaba1', 'uporaba2', 'uporaba3', 'kontinent']
#shrani = shrani_html()
preberi = preberi_dat_v_niz(stadioni_mapa, html_datoteka)
#print(preberi)
sez = seznam_nizov_oblike_rx(preberi)
#print(sez)
seznam = (seznam_stadionov(sez))
seznam_naborov = razclenjeni_stadioni(seznam)
slovar1 = slovar_stadionov(seznam_naborov)
slovar2 = dodaj_kontinente(slovar1, slovar_kontinentov)
zapisi_csv = zapisi_tabelo(slovar2, polja, csv_datoteka)
print(len(seznam_naborov))
#print(seznam_naborov)




