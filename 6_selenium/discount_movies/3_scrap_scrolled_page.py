# 활용3-2. Scrap all movies' title on the scrolled page
# selenium + bs4  /  6_handle_scroll.py + 5_bs4_dynamic.py

from selenium import webdriver
browser = webdriver.Chrome()
# browser.maximize_window()

url = "https://play.google.com/store/movies/top"
browser.get(url)

import time
interval = 2

prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    time.sleep(interval) 

    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")


import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title) 