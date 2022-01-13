from bs4 import BeautifulSoup
import requests

url = 'https://aliexpress.ru/item/1005001806483824.html?sku_id=12000017698985198&spm=a2g2w.productlist.0.0.6a1a1adeZPFypA'
# url = 'https://aliexpress.ru/item/4001193458040.html?spm=a2g2w.productlist.0.0.4793620coMJbLf'

# url = "https://aliexpress.ru/item/1005001465081562.html?spm=a2g20.search.0.0.5d9f39d7iO6QQb&algo_pvid=5d1dd444-7edd-4673-b275-d97a298ad63a&algo_expid=5d1dd444-7edd-4673-b275-d97a298ad63a-12" #hot


page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
name = soup.find('h1').get_text()
# products = soup.find("h1")

svoistva = soup.find('div', class_='Characteristics-styles_wrapper__2xHnh').find_all('span',
                                                                                     class_='ali-kit_Base__base__1odrub ali-kit_Base__light__1odrub')

svoistva_znach = soup.find('div', class_='Characteristics-styles_wrapper__2xHnh').find_all('span',
                                                                                           class_='ali-kit_Base__base__1odrub ali-kit_Base__default__1odrub')

result = []

data = [i.get_text(strip=True) for i in svoistva]
data2 = [i.get_text() for i in svoistva_znach]
data3 = dict(zip(data, data2))
print(data3)


file = "ali.txt"
f = open(file, 'a', encoding='utf-8')
#
i = 1
# for item in data3:
#     f.write(f'{i}. Название товара:  {item["name"]}, {item["svoistva"]} \n')
#     i += 1
f.write(name)
f.seek(0, 2)
for item in data3.items():
    f.write(f' {item[0]} {item[1]} ')
    i += 1
f.write("\n")
f.close()
#
# for item in svoistva:
#     print(f'свойства:{item.get_text()}')
# for zn in svoistva:
#      print(f'Название свойства:{zn.get_text()}')
