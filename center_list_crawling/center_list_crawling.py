from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome("./chromedriver")
driver.get("https://map.naver.com/v5/search")
# driver.get("https://map.naver.com/v5/?c=6,0,0,0,dh")

time.sleep(30)

# delete pop-up
driver.find_element_by_css_selector("button.btn_close.ng-tns-c190-13").click()

# search_keyword
search_keyword = "클라이밍"

# loading
search_box = driver.find_element_by_css_selector("div.input_box>input.input_search")
search_box.send_keys(search_keyword)
time.sleep(3)

search_box.send_keys(Keys.ENTER)
time.sleep(10)
print(driver.find_elements_by_css_selector("div.panel_wrap>div.XUrfU>ul>li.VLTHu.OW9LQ"))
print(len(driver.find_elements_by_css_selector("div.panel_wrap>div.XUrfU>ul>li.VLTHu.OW9LQ")))
