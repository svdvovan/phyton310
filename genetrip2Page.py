from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook
from tkinter import *
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

root = Tk()
root.geometry('850x200+1000+300')

fileName = 'genetrip2.xlsx'

l_url = Label(root, text="Введите url страницы категории:").grid(row=0, column=0, pady=10)
e_url = Entry(root, width=100)
e_url.grid(row=0, column=1, padx=15, sticky=E)

l_page = Label(root, text="Страницу с которой парсим:").grid(row=1, column=0, pady=10)
e_page = Entry(root, width=10)
e_page.insert(0, "1")
e_page.grid(row=1, column=1, padx=15, sticky=W)

l_lastPage = Label(root, text="Страницу по которую парсим:").grid(row=2, column=0, pady=10)
e_lastPage = Entry(root, width=10)
e_lastPage.insert(0, "1")
e_lastPage.grid(row=2, column=1, padx=15, sticky=W)

excel_file = Workbook()
excel_sheet = excel_file.create_sheet(title='genetrip2', index=0)

count = 2
countRow = 2


def bigParser(e_url, page, lastPage):
    global count
    global countRow

    for p in range(page, lastPage+1):
            if p==1:
                path2=e_url
            else:
                path2 = f'{e_url}?page={p}'
            print(path2)

            excel_sheet['A1'] = 'id'
            excel_sheet['B1'] = 'Название'
            excel_sheet['C1'] = 'Цена'
            excel_sheet['D1'] = 'Категория'
            excel_sheet['E1'] = 'Описание'
            excel_sheet['F1'] = 'Производитель'
            excel_sheet['G1'] = 'Главное фото'

            # countCol = 8
            # countFoto = 1
            # CountP = 1
            # CountPn = 20
            # CountPnZ = 21
            # CountPZZ = 1
            # largeFoto2 = []

            # for url in path2:
                # print(url)
            page = requests.get(path2, verify=False)
            soupCategory = BeautifulSoup(page.content, 'html.parser')
            # print(soupCategory)
            allProductInCategory = soupCategory.find_all('div', class_='product-name')
            for a in allProductInCategory:
                for link in a.find_all('a'):
                    # print(link.get('href'))
                    productPage=[]
                    productPage2 = (link.get('href'))
                    productPage.append(productPage2)
                    for p2 in productPage:
                        countCol = 8
                        countFoto = 1
                        CountP = 1
                        CountPn = 20
                        CountPnZ = 21
                        CountPZZ = 1
                        largeFoto2 = []

                        print(p2)
                        pageTovar = requests.get(p2, verify=False)
                        soup = BeautifulSoup(pageTovar.content, 'html.parser')

                        name = soup.find('h1', class_='h1-prod-name').getText()
                        mainFoto = soup.find('a', id="zoom1").get('href')
                        # foto = soup.find('div', class_='image-additional owl-carousel').find_all('a',
                        #                                                                          class_='thumbnail')
                        # category_for_post = soup.find('span', class_='posted_in').find('a').getText()
                        id = soup.find(itemprop="model").getText()
                        price = soup.find('span',
                                          class_='autocalc-product-price').getText()
                        try:
                            manufac = soup.find(itemprop="brand").getText()
                        except:
                            manufac = 'noBrand'
                        finally:
                            description1 = soup.find('div', id='tab-description')
                            description = str(description1)
                            svoistva = soup.find('table', class_='table table-bordered').find_all('td',
                                                                                                  itemprop='name')

                            svoistva_znach = soup.find('table', class_='table table-bordered').find_all('td',
                                                                                                        itemprop='value')
                            print(id)
                            print(manufac)
                            print(description)
                            print(price)
                            print(name)
                            #
                            excel_sheet[f'A{count}'] = id
                            excel_sheet[f'B{count}'] = name
                            excel_sheet[f'C{count}'] = price
                            # excel_sheet[f'D{count}'] = category_for_post
                            excel_sheet[f'E{count}'] = description
                            excel_sheet[f'F{count}'] = manufac
                            excel_sheet[f'G{count}'] = mainFoto

                            # for f in foto:
                            #     largeFoto = f['href']
                            #     largeFoto2.append(largeFoto)
                            # print(largeFoto2)
                            #
                            # for fot in largeFoto2:
                            #     excel_sheet.cell(row=1, column=countCol).value = f'фото{countFoto}'
                            #     excel_sheet.cell(row=countRow, column=countCol).value = fot
                            #     countFoto += 1
                            #     countCol += 1

                            datas = [i.get_text(strip=True) for i in svoistva]
                            datas2 = [i.get_text() for i in svoistva_znach]

                            for data in datas:
                                excel_sheet.cell(row=1, column=CountPn).value = f'Свойство {CountP}'
                                excel_sheet.cell(row=countRow, column=CountPn).value = data.replace(':', '')
                                CountP += 1
                                CountPn += 2

                            for data2 in datas2:
                                excel_sheet.cell(row=1, column=CountPnZ).value = f'Значение {CountPZZ}'
                                excel_sheet.cell(row=countRow, column=CountPnZ).value = data2
                                CountPnZ += 2
                                CountPZZ += 1

                            count += 1
                            countRow += 1

                    excel_file.save(fileName)


def getUrl():
    urls = e_url.get()
    page = int(e_page.get())
    # print(page)
    lastPage = int(e_lastPage.get())
    # print(lastPage)
    # print(urls)
    bigParser(urls, page, lastPage)
    #bigParser(urls)


l_start = Button(root, text="Парсить", command=getUrl).grid(row=4, column=0, padx=10, pady=10, sticky=W)
l_clear = Button(root, text="Очистить", command=lambda: e_url.delete(0, END)).grid(row=4, column=1, padx=0, pady=10,
                                                                                   sticky=W)
l_close = Button(root, text="Закрыть", command=lambda: root.destroy()).grid(row=4, column=1, padx=20, pady=10, sticky=E)
root.mainloop()
