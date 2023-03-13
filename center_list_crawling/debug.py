import time
import json

from io import TextIOWrapper
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# 크롬 드라이버 실행
def get_driver():
  options = webdriver.ChromeOptions()
  # 지정한 user-agent로 설정
  options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664 Safari/537.36") 
  # 크롬 화면 크기를 설정(but 반응형 사이트에서는 html요소가 달라질 수 있음)
  options.add_argument("window-size=1440x900")
  # 브라우저가 백그라운드에서 실행됩니다.
  # options.add_argument("headless")

  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)  # chromedriver 열기
#   driver = webdriver.Chrome("./chromedriver")
  driver.get('https://map.naver.com')  # 주소 가져오기
  driver.implicitly_wait(60)
  return driver

# 검색어 입력
def search_place(driver:WebDriver, search_text: str):
  print("search_place")
  search_input_box = driver.find_element_by_css_selector("div.input_box>input.input_search")
  search_input_box.send_keys(search_text)
  search_input_box.send_keys(Keys.ENTER)
  time.sleep(5)

# 다음 페이지 이동 및 마지막 페이지 검사
def next_page_move(driver:WebDriver):
  print("next_page_move")
  # 페이지네이션 영역에 마지막 버튼 선택
  next_page_btn = driver.find_element_by_css_selector('div.zRM9F>a:last-child')
  next_page_class_name = BeautifulSoup(next_page_btn.get_attribute('class'), "html.parser")

  if len(next_page_class_name.text) > 10:
    print("검색완료")
    driver.quit()
    return False
  else:
    next_page_btn.send_keys(Keys.ENTER)
    return True

# 검색 iframe 이동
def to_search_iframe(driver:WebDriver):
  print("to_search_iframe")
  # 이 과정에서 5개만 찾고 못찾는 버그 있음
  driver.switch_to.default_content()
  driver.switch_to.frame('searchIframe')

# element 텍스트 추출
def get_element_to_text(element):
  print("get_element_to_text")
  return BeautifulSoup(element, "html.parser").get_text()

# 매장정보 추출
def get_store_data(driver:WebDriver, scroll_container: WebElement, file: TextIOWrapper):
  print("get_store_data")
  # 현재 페이지 매장 리스트
  get_store_li = scroll_container.find_elements_by_css_selector('ul > li')
  
  for index in range(len(get_store_li)):
    # json 파일 저장 init
    # 매장 이름, 네이버 카테고리, 주소, url, 메인 사진 url, 가격, 시간, 레벨, 바뀌는 주기
    json_data = {}
    json_list = ['store_name', 'naver_category', 'address', 'naver_map_url', 'main_img_url', 'price_list', 'open_time', 'level', 'change_time']
    store_name = naver_category = address = naver_map_url = main_img_url = price_list = open_time = level = change_time = ''
    json_var_list = [store_name, naver_category, address, naver_map_url, main_img_url, price_list, open_time, level, change_time]
    
    
    selectorArgument = 'div:nth-of-type(1) > div.ouxiq.icT4K > a:nth-child(1)'
    wrapper_html = get_store_li[index].get_attribute('innerHTML')
    wrapper_soup = BeautifulSoup(wrapper_html, "html.parser")

    # 매장 항목 클릭
    get_store_li[index].find_element_by_css_selector(selectorArgument).click()

    # 매장 상세로 iframe 이동
    driver.switch_to.default_content()
    driver.switch_to.frame('entryIframe')

    time.sleep(3)

    try:
      try: 
        WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CLASS_NAME, "place_didmount")))
      except TimeoutException:
        to_search_iframe(driver)
        
      # 매장 이름, 네이버 카테고리, 주소, url, 메인 사진 url, 가격, 시간, 레벨, 바뀌는 주기
      
      # 매장 이름
      store_name = driver.find_element_by_css_selector('#_title > span:nth-child(1)').get_attribute('innerHTML')

      # 네이버 카테고리
      if driver.find_element_by_css_selector('#_title > span:nth-child(2)').is_displayed():
        naver_category = driver.find_element_by_css_selector('#_title > span:nth-child(2)').get_attribute('innerHTML')
      else:
        naver_category = ''
      
      # 주소
      address = driver.find_element_by_css_selector('div > a > span.LDgIH').get_attribute('innerHTML')
      
      # url
      naver_map_url = driver.current_url
      
      # 메인 사진 url
      tmp = str(wrapper_soup)
      main_img_url = tmp.split('src="')[1].split('"')[0]
      print("메인 이미지 url")
      print(main_img_url)
      # 가격
      price_list = driver.find_element(By.CSS_SELECTOR, "div.O8qbU.tXI2c > div > ul > li").text
      print("가격 리스트")
      print(price_list)
      # 시간
      
      # 레벨
      # 바뀌는 주기
      
      
      # store_name, naver_category, address, naver_map_url, main_img_url, price_list, open_time, level, change_time
      store_name = get_element_to_text(store_name)
      naver_category = get_element_to_text(naver_category)
      address = get_element_to_text(address)
      price_list = get_element_to_text(price_list)
      
      
      for i in range(len(json_list)):
          json_data.update({json_list[i]: json_var_list[i]})
      
      with open('list.json', 'w') as f:
          json.dump(json_data, f, indent=2)
      to_search_iframe(driver)
    except TimeoutException:
      to_search_iframe(driver)

# 메인 함수
def naver_crawl():
  filer = open('./list.json','a',encoding='utf-8')
  driver = get_driver()
  search_place(driver,'클라이밍')
  to_search_iframe(driver)
  time.sleep(2)

  try:
    scroll_container = driver.find_element_by_id("_pcmap_list_scroll_container")
  except:
    print("스크롤 영역 감지 실패")

  try:
    while True:
      for i in range(6):
        # 스크롤 내리는 자바 스크립트 코드 실행
        driver.execute_script("arguments[0].scrollBy(0,2000)",scroll_container)
        time.sleep(1)
      get_store_data(driver,scroll_container,filer)
      is_continue = next_page_move(driver)
      if is_continue == False:
        break
  except:
    print("크롤링 과정 중 에러 발생")
    
naver_crawl()