# Print all (movie's) img url on "res" [daum]

# < Basic Frame >
import requests
from bs4 import BeautifulSoup
# This link : site to work
res = requests.get(
    "https://search.daum.net/search?w=tot&q=2020%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR")
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")


images = soup.find_all("img", attrs={"class": "thumb_img"})

for image in images:
    print(image["src"])
