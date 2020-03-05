import requests
from SearchList import getSearchList
from Tools import replaceSRC

savePath="C:\\node_work\\public\\news\\"

search_list = getSearchList("https://news.naver.com/", "ul.hdline_article_list")
div_list = search_list[0].find_all('div', class_='hdline_article_tit')
for i, element in enumerate(div_list):
    newsUrl = "https://news.naver.com" + element.find("a")["href"]
    imgTags = getSearchList(newsUrl, "div#articleBodyContents img")
    newsContents = getSearchList(newsUrl, "div#articleBodyContents")[0]

    srcList = []
    for j, img in enumerate(imgTags):
        src = img.get("src")
        response = requests.get(src[:src.index("?")])
        assert response.status_code is 200

        imgName = "tmp_img" + str(i) + str(j) + ".jpg"
        srcList.append(imgName)
        with open("savePath"+imgName, "wb") as fp:
            fp.write(response.content)

    newsContents = replaceSRC(str(newsContents), srcList)
    with open("savePath+newsContent"+str(i)+".html", "w", encoding="utf8") as fp :
        fp.write(newsContents)