# << Basic Frame >>
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")


# << bs4 활용편0 : Get all title of naver webtoon >>
# Find all elements which meet the bracket[condition]
# The condition : Find all the elements whose tag are "a" tag and class are "title".
cartoons = soup.find_all("a", attrs={"class": "title"})
for cartoon in cartoons:
    print(cartoon.get_text())
