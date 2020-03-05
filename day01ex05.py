import time

import requests
from bs4 import BeautifulSoup


response = requests.get("https://news.naver.com/")
assert response.status_code is 200

dom = BeautifulSoup(response.content, 'html.parser')

headline = dom.select("ul.hdline_article_list")
# select() 의 결과는 리스트 타입이다.
print(headline)

hdline_list = headline[0].find_all("div", class_="hdline_article_tit")
print(hdline_list)

# 파일명, 모드 인코딩
fp=open("hdline_list.txt","w",encoding="utf8")
for i, element in enumerate(hdline_list):
    # print(i, element.find("a").text.strip())
    # print(">>>>>>", element.find("a")['href'])
    a = element.find("a");
    data = "{}|{}|{}".format(i, a.text.strip(), a['href'])
    fp.write(data+"\n")

fp.close()

fp = open("hdline_list.txt", "r", encoding="utf8")
lines = fp.readline()
for line in lines:
    line = line.strip()
    li = line.split("|")
    print(li[0], li[1])
    print(">>>>>>>", li[2])

fs=open("hdline_list.txt","w",encoding="utf8")
for i, element in enumerate(hdline_list):
    # print(i, element.find("a").text.strip())
    # print(">>>>>>", element.find("a")['href'])
    a = element.find("a");
    data = "{}|{}|{}".format(i, a.text.strip(), a['href'])
    fp.write(data+"\n")

fs.close()

fs = open("hdline_list.txt", "r", encoding="utf8")
lines = fs.readline()
for line in lines:
    line = line.strip()
    li = line.split("|")
    print(li[0], li[1])
    print(">>>>>>>", li[2])