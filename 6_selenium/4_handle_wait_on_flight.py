# 활용2. Scraping obj[site] : Naver flight ticket.

# 1st goal. How to handle the loading time after searching for a flight ticket (Can't Expect how long it will take)
# 2nd goal. Scrap the result info.

from selenium import webdriver
browser = webdriver.Chrome()
# browser.maximize_window()  # Maximize chrome.

url = "https://flight.naver.com"
browser.get(url)

# < Click "가는 날" btn >
# browser.find_element_by_link_text("가는 날").click() # ?? Why not work
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()

# ( To find another way of c001 with link_text but all failed )
# elem = browser.find_elements_by_link_text("29")
# print(elem) # ?? why empty
# elem = browser.find_elements_by_link_text("29")[0]
# print(elem)
# elem = browser.find_element_by_link_text("29")
# print(elem)
# print(browser.find_element_by_partial_link_text("29"))
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[6]/button/b").click()
# browser.find_element_by_class_name("sc-crzoAE hnpClg inner start_end").click()
# ==> 💥 Give up to set date💥 But there is answer of goals
# I think computer can't recognize the small window of choosing date

# < Set date >
# browser.find_elements_by_link_text("29")[0].click() # c001 # visiting date / [0] : This month ; 1st 27
browser.find_element_by_link_text("당일").click()
browser.find_elements_by_link_text("4")[0].click() # return date / [1] ; Next month

#----------------------------------------------------------------------------------

# < The answer of 1st goal to go to 2nd goal > : 로딩 중에는 (로딩 후에 나오는) 엘레멘트를 찾을 수 없으니 끝나고 처리하기

# < Before handing loading >
# elem = browser.find_element_by_xpath("")
# print(elem.text)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# WebDriverWait(what, how long) / 10: 10 지나기 전에 로딩 끝나서 ""에 해당되는 엘레멘트가 발견되면  바로 실행됨 [그만 기다림], 10초 지나도 로딩 중이면 에러남  
# EC.presence_of_all_elements_located((무엇을 기다릴지)) : 빈칸의 엘레멘트가 위치할[나올] 때까지 기다려라
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, "")))
    print(elem.text) # >> Print[Scrap] 1st result[flight info] / If the code just above doesn't occur error, this code will be run.
finally: # try 안의 코드가 에러났을 때 또는 모든 코드가 실행 됐을 때
    browser.quit()