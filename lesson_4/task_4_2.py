
import requests
from bs4 import BeautifulSoup




dollar_rub = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
euro_rub = 'https://www.google.com/search?q=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&sxsrf=ALeKk01yFMkXbQs0dB3BuUgU4V2MZHM6YA%3A1617000695415&ei=93hhYI_ZGKKLwPAPsvqVoAk&oq=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=Cgdnd3Mtd2l6EAMyBwgAELEDEEMyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6BwgAEEcQsAM6BwgAELADEEM6BggAEAcQHjoICAAQBxAKEB46BAgAEA1Qy6PeA1iip94DYPOr3gNoAnACeACAAXCIAZIEkgEDMC41mAEAoAEBqgEHZ3dzLXdpesgBCsABAQ&sclient=gws-wiz&ved=0ahUKEwjPsLSA9dTvAhWiBRAIHTJ9BZQQ4dUDCA0&uact=5'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}



full_pages_dollar = requests.get(dollar_rub, headers = headers)
soup_dollar = BeautifulSoup(full_pages_dollar.content, 'html.parser')
convert_dollar = soup_dollar.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": "2"})
print('1 доллар США равно', convert_dollar[0].text, 'рублей')

full_pages_euro = requests.get(euro_rub, headers = headers)
soup_euro = BeautifulSoup(full_pages_euro.content, 'html.parser')
convert_euro = soup_euro.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": "2"})
print('1 евро равно', convert_euro[0].text, 'рублей')