# 활용3-1. How to handle scroll

from selenium import webdriver
browser = webdriver.Chrome()
# browser.maximize_window()

# < page movement >
url = "https://play.google.com/store/movies/top"
browser.get(url)

# < Scroll down to the designated location[coordinates] >
# browser.execute_script("window.scrollTo(0, 1080)") 
# javascript makes web dynamic. / 1920 x 1080 / scrollTo(어디까지) : 세로 방향으로 모니터[해상도] 높이인 1080 위치로 스크롤을 내려라

# ❗❗ KEY CODE ❗❗ 
# < Repeat scrolling down to the bottom of the screen until no more movie [until can't scroll down / until the height of scroll bar doesn't change] >
import time
interval = 2 # To scroll down every 2s

prev_height = browser.execute_script("return document.body.scrollHeight") # Get curr scroll pos / c001

while True:
    # Scroll down to the bottom of the screen. 
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # To waiting for page loading after scrolling down by the code just above
    time.sleep(interval) 

    # Get scroll pos after scrolling down [loading; the code just above]
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height: # no more movies
        break

    prev_height = curr_height # prev_height = 0 (c001 / Before scrolling down [loading]) -> like 1000 (after the 1st scroll) -> like 200 (after the 2nd one)

print("스크롤 완료")
