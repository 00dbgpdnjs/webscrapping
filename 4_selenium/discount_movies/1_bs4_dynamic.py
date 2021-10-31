# 활용3. Scraping movie title
# Check two problems on print(len(movies)) with bs4 before scraping[handling] dynamic page with selenium

# - dynamic page : It will be run When a user does something.
# - ex) When the user scrolls down, the new list is updated.

import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top" # 인기차트 on goole movie
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50",
    "Accept-Language":"ko-KR,ko" # Request for a page in Korean language. (If the server has a Korean page, return it, and if not, return the basic page.)
    }

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"}) # This condition[bracket] is the top[highest] elements that point to each movie.
print(len(movies)) # A total of movies[elems] / >> 0 (Before declaring "headers") / >> 10 (After declaring "headers")

# ❗❗ KEY CODE ❗❗
# < Why print(len(movies)) is 0 >
# - Google Movie returns different pages based on header info (not user agent info) of the user[korean, requests..] who accesses.
# - When korean accesses, it's for Korea, and when "requests" accesses, it's for America(default).
# - Solution: Declare "headers" to get "requests" the Korean page.
# < Why print(len(movies)) is 10 >
# - cuz it's a dynamic page. (The site show the initial 10 movies and is loaing) 

# Makes soup obj's text  html file to check if there's text what you want. If not, put useragent or use selenium
# with open("movie.html", "w", encoding="utf-8") as f:
#     # f.write(res.text)
#     f.write(soup.prettify()) # Write "soup" html pretty

# < Print all movies's title >
for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title) 