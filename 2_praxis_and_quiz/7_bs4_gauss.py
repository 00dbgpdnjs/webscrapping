# << Basic Frame >>
import requests
from bs4 import BeautifulSoup

# "가우스전자" among naver webtoon
url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")


# << bs4 활용편1 : Get title and its link  of the last[latest] ep of 가우스전자 >>
cartoons = soup.find_all("td", attrs={"class": "title"})
# "cartoons" is lst which has all ep. cartoons[0] is last[latest] ep
title = cartoons[0].a.get_text()
link = cartoons[0].a["href"]
print(title)
print("https://comic.naver.com" + link)


# << Get all titles and the links  of all ep of first page of 가우스전자 webtoon  >>
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)


# << bs4 활용편1-1 : average rating(평점) of all ep of fist page of 가우스전자 >>
# total_rates = 0
# cartoons = soup.find_all("div", attrs={"class": "rating_type"})
# for cartoon in cartoons:
#     rate = cartoon.find("strong").get_text()
#     print(rate)
#     total_rates += float(rate)  # float() change string[bracket] to float
# print("전체 점수 : ", total_rates)
# print("평균 점수 : ", total_rates / len(cartoons))
