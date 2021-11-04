# What we do on this file : How to get element or part of element  of website with beautifulsoup4

# bs4 : $ pip install beautifulsoup4 # package for scraping
# $ pip install lxml # lxml is a parser to analyze syntax

import requests
from bs4 import BeautifulSoup

# Refer this paragraph to 2_requests.py
url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

# 1st arg: html text / lxml parser makes the text beautifulsoup obj
soup = BeautifulSoup(res.text, "lxml")



# --------------------------------------------------------------------------
# ❗❗ KEY LINE ❗❗ So far, 6 codes are basic frame for "soup".
#                From under, get element of website  with "soup" var


# print(soup.title)  # Print title element among soup
# print(soup.title.get_text()) # Print content of title tag
# print(soup.a)  # Print only the first a element
# print(soup.a.attrs)  # Print attributes of a tag to dictionary form
# print(soup.a["href"])  # Print value of href attr of a tag

# Find first element / var[soup]에서 원하는 element를 얻기위해  put condition in bracket
# print(soup.find("a", attrs={"class": "Nbtn_upload"}))

# < find_all() >
# dust.find_all("li")[0].get_text().strip()
# soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=3) # limit with loop

# < several class condition >
# soup.find("dl", attrs={"class":["ImZGtf mpg5gc", "Vpfmgd"], "id":"dust"}, text=["미세먼지", "초미세먼지"]

rank1 = soup.find("li", attrs={"class": "rank01"})
# print(rank1.a) # Print only "a" element of "'rank1'[li tag] soup obj"
# soup.find("a", text="독립일기-11화 밥공기 딜레마") : tag의 attrs로가 아닌 tag 사이의 content로 element를 얻으려면

# << How to find sibling >> : rank1~3 are siblings
# print(rank1.a.get_text())
# print(rank1.next_sibling) # If nothing is printed, enter 'rank1.next_sibling.next_sibling' because of linespacing
# rank2 = rank1.next_sibling.next_sibling
# rank2 = rank1.find_next_sibling("li") # This func: Find the 1st li tag among rank1's next sibling tags. / Unlike "next_sibling", no need to worry about linespacing. So no need to think about  how many times I enter next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())

# rank2 = rank3.previous_sibling.previous_sibling
# rank2 = rank3.find_previous_sibling("li") # same with the code just above. The difference is this code is except to linespacing  by finding only li tag
# print(rank2.a.get_text())


# << How to find parent tag >>
# print(rank1.parent)

# << How to find all siblings >>
# Find all li element among rank1's sibling elements
print(rank1.find_next_siblings("li"))
