from bs4 import BeautifulSoup
import urllib.request
import ssl

context = ssl._create_unverified_context()
req = urllib.request.urlopen("https://fitlife62.ru/sportivnye-leginsy/", context=context)
html = req.read()
file = "parser.txt"
f = open(file, 'w', encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')


Goods = soup.find_all('div', class_="product-thumb product-wrapper")


result = []
for item in Goods:
    nameGoods = item.find('h4', class_='name').get_text()
    href = item.a.get('href')
    result.append({
        'name': nameGoods,
        'href': href
    })

i = 1
for item in result:
    f.write(f'{i}. Название товара:  {item["name"]}, Ссылка на товар: {item["href"]}\n')
    i += 1

f.close()
