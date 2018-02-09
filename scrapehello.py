
from bs4 import BeautifulSoup

f = open("hello.html")
html = f.read()
soup = BeautifulSoup(html, 'html.parser')



all_goodbye_elements = soup.find_all(class_='goodbye')
print('goodbye elements:', all_goodbye_elements)
print('------')





width_tag = soup.find_all('img')
print('The img width:')
print(width_tag)
print('------')


url_item = soup.find_all('a')
print(url_item)
