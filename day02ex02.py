from bs4 import BeautifulSoup
from selenium import webdriver
import time

path='/chromedriver'
driver=webdriver.Chrome(path)
driver.get('http://www.naver.com')

time.sleep(1)

driver.find_element_by_css_selector('#PM_ID_serviceNavi > li:nth-child(2) > a > span.an_icon').click()
