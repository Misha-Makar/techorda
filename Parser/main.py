import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
import sqlite3

data = []
for p in range(1, 24):
    print(p)
    url = (
        f'https://krisha.kz/arenda/kvartiry/astana/?das[_sys.hasphoto]=1&das[live.furniture]=1&das[live.rooms]=1&das[live.square][from]=36&das[live.square][to]=39&das[who]=1&rent-period-switch=%2Farenda%2Fkvartiry&page={p}')
    r = requests.get(url)
    sleep(2)

    soup = BeautifulSoup(r.text, 'lxml')
    section = soup.find('section', class_='a-list a-search-list a-list-with-favs')
    flats = section.findAll('div', class_='a-card__inc')
    print(len(flats),'flat')
    for flat in flats:
        try:
            links = 'https://krisha.kz' + flat.find('a', class_='a-card__title').get('href')
        except:
            links = '-'

        try:
            names = flat.find('a', class_='a-card__title').string
        except:
            names = '-'

        try:
            prices = flat.find('div', class_='a-card__price').text
        except:
            prices = '-'

        try:
            locations = flat.find('div', class_='a-card__subtitle').text
        except:
            locations = '-'

        try:
            owners = flat.find('div', class_='owners__label owners__label--yellow label-user-owner').text
        except:
            owners = '-'

        try:
            cities = flat.find('div', class_='card-stats__item').text
        except:
            cities = '-'

        try:
            pub_dates = flat.findAll('div', class_='card-stats__item')[1].text
        except:
            pub_dates = '-'

        try:
            description = flat.find('div', class_='a-card__text-preview').text
        except:
            description = '-'

        data.append([links, names, prices, locations, owners, cities, pub_dates, description])

header = ['links', 'names', 'prices', 'locations', 'owners', 'cities', 'pub_dates', 'description']
df = pd.DataFrame(data, columns=header)


table_name = 'OneRoomFlatRent'
conn = sqlite3.connect('mydb.sqlite')
query = f'Create table if not Exists {table_name} (Name text, Course text, Age real)'
conn.execute(query)
df.to_sql(table_name,conn,if_exists='replace',index=False)
conn.commit()
conn.close()

# git init
# git add .
# git commit -m "First commit"
# #Go to https://github.com --- Create a new repository (without README.md)
# git remote add origin https://github.com/Misha-Makar/techorda
# git push -u origin master