# 활용3-4. headless chrome 
# = Chrome without chrome / Work chrome on background [internally]

from selenium import webdriver

# ❗❗ KEY CODE ❗❗ 

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080") # Set up size internally.

browser = webdriver.Chrome(options=options) 
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

# Can take screenshot of headless chrome at this time
browser.get_screenshot_as_file("google_movie.png") 



import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title, "    <할인 중이 아닌 영화이다>")
        continue
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    link = movie.find("a", attrs={"class":"JC71ub"})["href"]

    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : ", "https://play.google.com" + link)
    print("-" * 100)

browser.quit()