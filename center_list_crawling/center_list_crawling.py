from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

# search_keyword
search_keyword = "클라이밍"

driver = webdriver.Chrome("./chromedriver")
driver.get("https://map.naver.com/v5/?c=6,0,0,0,dh")


# loading
search_box = driver.find_element_by_css_selector("div.input_box>input.input_search")
search_box.send_keys(search_keyword)

time.sleep(3)

# 검색버튼 누르기
search_box.send_keys(Keys.ENTER)
