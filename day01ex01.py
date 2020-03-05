import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.naver.com/")
assert response.status_code is 200

# print(response.text)

dom = BeautifulSoup(response.content, "html.parser")
print(dom)