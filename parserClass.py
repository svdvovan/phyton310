from bs4 import BeautifulSoup
import urllib.request
import ssl


class myParser:
    # file = "parser.txt"
    context = ssl._create_unverified_context()

    def __init__(self, url, saveFile=1, file="parser.txt"):
        self.url = url
        self.saveFile = saveFile
        self.file = file

    def beginParser(self):
        # context = ssl._create_unverified_context()
        req = urllib.request.urlopen(self.url, context=self.context)
        html = req.read()
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

        if self.saveFile == 1:
            f = open(self.file, 'w', encoding='utf-8')
            i = 1
            for item in result:
                f.write(f'{i}. Название товара:  {item["name"]}, Ссылка на товар: {item["href"]}\n')
                i += 1
            f.close()
        else:
            for item in result:
                print(f'"Название товара:  {item["name"]}, Ссылка на товар: {item["href"]}\n')

#
# startParser = myParser("https://fitlife62.ru/sportivnye-leginsy/", 1, "my.txt")
# startParser.beginParser()
