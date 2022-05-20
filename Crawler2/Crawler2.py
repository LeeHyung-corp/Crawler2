from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import csv
import io

f= open('코스피.csv', 'rt', encoding='UTF8')
rdr = csv.reader(f)

constant = 86400000

time.sleep(15)

driver = webdriver.Chrome('C:\\Users\\luke2\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.implicitly_wait(3)
driver.get('http://hogaplay.com/player/')
input() #잠시 중지

tabs = driver.window_handles


for line in rdr:
    for stocks in line[1:]: #모든 주식에 대해
        for i in tabs:
            driver.switch_to.window(i)
            driver.implicitly_wait(3)
            search_input = driver.find_element_by_xpath('//input[@id="NameInput"]') #종목명 입력
            search_input.send_keys(stocks)
            search_input.send_keys(Keys.ENTER)
            driver.implicitly_wait(3)
            time.sleep(random.randint(100,120)/100)

            search_input = driver.find_element_by_xpath('//button[@id="ContractDownload"]') #다운로드 요청
            driver.implicitly_wait(3)
            search_input.click()
        time.sleep(random.randint(400,500)/100)

#for i in tabs:
#    driver.switch_to.window(i)
#    for line in rdr:
#        for stocks in line:

#for line in rdr:
#    date = 1602633600000 + (int(line[0][-2:])-14)*86400000
#    search_input = driver.find_element_by_xpath('//button[@id="DateButton"]') #캘린더 클릭
#    search_input.click()
#    search_input = driver.find_element_by_xpath('//td[@data-date="' +str(date)+ '"]')
#    search_input.click()
#    driver.implicitly_wait(3)
#    time.sleep(random.randint(100,120)/100)
#    for stocks in line[1:]:
#        search_input = driver.find_element_by_xpath('//input[@id="NameInput"]') #종목명 입력
#        driver.implicitly_wait(3)
#        search_input.send_keys(stocks)
#        search_input.send_keys(Keys.ENTER)
#        time.sleep(random.randint(100,120)/100)

#        search_input = driver.find_element_by_xpath('//button[@id="ContractDownload"]') #다운로드 요청
#        driver.implicitly_wait(3)
#        search_input.click()
#        time.sleep(random.randint(300,400)/100)





f.close()

#search_input = driver.find_element_by_xpath('//td[@data-date="1600905600000"]')
#search_input.click()

time.sleep(100)

#for i in range(0,100):
#   웹크롤링 코드
#   time.sleep(random.randint(3, 7))

#<input type="text" class="form-control" id="NameInput" placeholder="종목명" autocomplete="off">
#$x('//input[@id="NameInput"]')