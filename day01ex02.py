'''
크롤링 가능한 기술 : JAVA, Node, js, Python...
1) 지정된 url에서 html 문서를 읽어온다.(requests)
2) 읽어 들인 문서를 html 페이지로 파싱 한다.(html.parser)
3) 파싱 된 데이터를 다시 검색 가능한 동적 DOM 형태로 변환한다(BeautifulSoup)

필요한 모듈
requests: 지정된 url에서  html페이지를 바이트 코드로 불러온다.
LxmL 또는 html.parser : Lxml 은 모듈을 설치 해야 사용가능
BeautifulSoup: CSS 나 jQuery 의 셀렉터처럼 사용 할수 있게 해 준다.(DOM 형식)

[requests 객체의 중요 모듈]
response.headers : 응답 페이지의 헤더 정보를 딕셔너리로 저장 되었다.
response.encording : 인코딩 정보
response.text : 응답 페이지의 소스 코드 내용 ( 실제 페이지의 소스코드)
response.content : 응답 페이지의 내용을 바이트 코드로 불러온다.
response.json(): JSON 형식으로 불러온다.

BeautifulSoup :
https://www.crummy.com/software/BeautifulSoup/bs4/doc/

'''

import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.naver.com/")
assert response.status_code is 200

# print(response.text)



dom = BeautifulSoup(response.content, "html.parser")
print(dom)

print(type(dom))
# 태그를 직접 접근하기
print(dom.title)
# print(dom.title.text)
print(dom.head.string)

print(type(dom.head.text)) # str
print(type(dom.title.string)) # bs4.element.NavigableString
print(type(dom.title))# bs4.element.Tag

'''
[태그와 관련된 속성 둘]
contents: 리스트 형식으로 자식 태그를 가져온다. (dom.태그.contents)
children : 이터레이터 형태로 자식 태그를 가져온다. (dom.태그.children)
parnets : 제너레이털 형태로 부모 태그를 가져온다. (dom.태그.parnets)
next_sibling : 다음 형제 태그
previous_sbling : 이전 형제 태그
next_element : 다음 요소 접근
previous_element : 이전 요소 접근
'''




