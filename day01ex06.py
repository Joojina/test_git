import time
import requests
from SearchList import getSearchList

search_list = getSearchList("https://news.naver.com/", "ul.hdline_article_list")
div_list = search_list[0].find_all('div', class_='hdline_article_tit')
for i, element in enumerate(div_list):
    imgTags = getSearchList("https://news.naver.com" + element.find("a")["href"], "div#articleBodyContents img")

    for j, img in enumerate(imgTags):
        src = img.get("src")
        response = requests.get(src[:src.index("?")])
        assert response.status_code is 200

        with open("news_img/tmp_img" + str(i) + str(j) + ".jpg", "wb") as fp:
            fp.write(response.content)
