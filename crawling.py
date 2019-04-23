import requests
from bs4 import BeautifulSoup
import json
import os

##python 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

##HTTP GET Request
req = requests.get('https://beomi.github.io/beomi.github.io_old/')

#html 소스 가져오기
html = req.text
## BeautifulSoup으로 html소스를 python객체로 변환하기
## 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시.
## 이 글에서는 Python 내장 html.parser를 이용했다.

soup = BeautifulSoup(html, 'html.parser')
## string list가 아니라 soup객체의 list이다.
my_titles = soup.select (
    'h3 > a'
)

data = {}

for title in my_titles:
    data[title.text] = title.get('href')

with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    json.dump(data, json_file)
    
'''
my_title는 list 객체
for title in my_titles:
    ##Tag안의 텍스트
    print(title.text)
    ##Tag의 속성을 가져오기 ex) href
    print(title.get('href'))
'''