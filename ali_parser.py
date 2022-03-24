import json

from bs4 import BeautifulSoup
import requests
import pickle
import csv
import pandas as pd
import openpyxl


# url = 'https://aliexpress.ru/item/1005001806483824.html?sku_id=12000017698985198&spm=a2g2w.productlist.0.0.6a1a1adeZPFypA'
# url = 'https://aliexpress.ru/item/4001193458040.html?spm=a2g2w.productlist.0.0.4793620coMJbLf'
from openpyxl import Workbook

#url = 'https://aliexpress.ru/item/1005001568107064.html?_evo_buckets=165609%2C165598%2C188873%2C194277%2C224411%2C224373%2C176818&_t=gps-id%3ApcDetailLeftTopSell%2Cscm-url%3A1007.13482.95643.0%2Cpvid%3A9a7ce2d0-e902-4b5a-995f-7a7ac9efbfa6%2Ctpp_buckets%3A21387%230%23233228%237&gps-id=pcDetailLeftTopSell&pvid=9a7ce2d0-e902-4b5a-995f-7a7ac9efbfa6&scm=1007.13482.95643.0&scm-url=1007.13482.95643.0&scm_id=1007.13482.95643.0&sku_id=12000016622436063&spm=a2g2w.detail.100009.1.13a57598b6voAV'

#url = 'https://aliexpress.ru/item/1005001465081562.html?spm=a2g20.search.0.0.5d9f39d7iO6QQb&algo_pvid=5d1dd444-7edd-4673-b275-d97a298ad63a&algo_expid=5d1dd444-7edd-4673-b275-d97a298ad63a-12'
#url ='https://aliexpress.ru/item/1005001592825712.html?_evo_buckets=165609%2C165598%2C188872%2C194277%2C224411%2C224373%2C176818&_t=gps-id%3ApcDetailBottomMoreThisSeller%2Cscm-url%3A1007.13339.169870.0%2Cpvid%3Ad8a27357-3570-41a7-8c62-fdf5f9a172c9%2Ctpp_buckets%3A21387%230%23233228%2310&gps-id=pcDetailBottomMoreThisSeller&pvid=d8a27357-3570-41a7-8c62-fdf5f9a172c9&scm=1007.13339.169870.0&scm-url=1007.13339.169870.0&scm_id=1007.13339.169870.0&sku_id=12000016713342689&spm=a2g2w.detail.0.0.36fe4ab0ve7lA4'
url = 'https://aliexpress.ru/item/1005003556155048.html?_evo_buckets=165609%2C165598%2C188871%2C194277%2C224411%2C224373%2C176818&_t=gps-id%3ApcDetailBottomMoreThisSeller%2Cscm-url%3A1007.13339.169870.0%2Cpvid%3Aa3e45df8-7ac5-4603-b472-8ade50e24cb0%2Ctpp_buckets%3A21387%230%23233228%238&gps-id=pcDetailBottomMoreThisSeller&item_id=1005003556155048&pvid=a3e45df8-7ac5-4603-b472-8ade50e24cb0&scm=1007.13339.169870.0&scm-url=1007.13339.169870.0&scm_id=1007.13339.169870.0&sku_id=12000026278135346&spm=a2g2w.detail.1000013.1.663d1e95JTc5BA'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
name = soup.find('h1').get_text()
# products = soup.find("h1")

svoistva = soup.find('div', class_='Characteristics-styles_wrapper__2xHnh').find_all('span',
                                                                                     class_='ali-kit_Base__base__1odrub ali-kit_Base__light__1odrub')

svoistva_znach = soup.find('div', class_='Characteristics-styles_wrapper__2xHnh').find_all('span',
                                                                                           class_='ali-kit_Base__base__1odrub ali-kit_Base__default__1odrub')

foto = soup.find('div', class_='Product_GalleryBar__bar__156z6').find_all('img')

description1 = soup.find('div', class_='ProductDescription-module_content__1xpeo')

description = (str(description1)).replace("\n", '')
print(description)

largeFoto2 = []
for f in foto:
    largeFoto = f['src']
    largeFoto2.append(largeFoto.replace('_50x50.jpg', ''))

print(largeFoto2)

result = []
foto3 = [i for i in svoistva]
data = [i.get_text(strip=True) for i in svoistva]
data2 = [i.get_text() for i in svoistva_znach]
data3 = dict(zip(data, data2))

file = "ali.txt"
# f = open(file, 'a', encoding='utf-8')
#
# i = 1
# # f.write(f'{i} {name}')
# # f.seek(0, 2)
# i += 1
#
# for item in data3.items():
#     f.write(f' {item[0]} {item[1]} ')

# f.write(description)
#
# f.write("\n")
# f.close()



#
# fileName = r'ali.xlsx'
# nameDesc = pd.DataFrame([[name, description]])
# colNames = ['название', 'описание']
# nameDesc.to_excel(fileName, index=False, sep=';', encoding='cp1251', header=colNames)
#
# myString = pd.read_csv(fileName, sep=';', encoding='cp1251')
#
# for fot in largeFoto2:
#     myString[f'foto{n}'] = [fot]
#     n += 1
# myString.to_excel(fileName, index=False, sep=';', encoding='cp1251')


n = 1
p = 1

fileName = 'ali.xlsx'
nameDesc = pd.DataFrame([[name, description]])
colNames = ['название', 'описание']

nameDesc.to_excel(fileName, index=False, header=colNames)

myString = pd.read_excel(fileName)

for fot in largeFoto2:
    myString[f'foto {n}'] = [fot]
    n += 1
myString.to_excel(fileName, index=False)

# nameDesc.to_excel(fileName, startcol=27, startrow=1, index=False , sheet_name='ali')


# FIXME сделать разбивку свойства и значения свойства по столбцам
# TODO сделать с определенного столбца размещение свойств
myString1 = pd.read_excel(fileName)
for item in data3.items():
    myString1[f'свойство {p}'] = (f'{item[0]} {item[1]}')
    p += 1
myString1.to_excel(fileName,  index=False, sheet_name='ali')




# TODO парсинг нескольких товаров сразу (из массисва значений)
# TODO сделать как  десктопное приложение
