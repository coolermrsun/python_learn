import requests
import time
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'}

url = 'https://movie.douban.com/top250'
def top250(url):
    spond = requests.get(url,headers=headers)

    soup = BeautifulSoup(spond.text,'html.parser')

    all_title = soup.find_all("span",attrs={"class":"title"})

    for title in all_title:
        title_string = title.string
        if "/" not in title_string:
            print(title_string)
for i in range(0,250,25):
      url = f'https://movie.douban.com/top250?start={i}&filter='
      top250(url)
      time.sleep(2)