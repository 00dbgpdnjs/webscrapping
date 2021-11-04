# << Basic Frame >>
import requests
from bs4 import BeautifulSoup
# This link : site to work
res = requests.get(
    "https://search.daum.net/search?w=tot&q=2020%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR")
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")


images = soup.find_all("img", attrs={"class": "thumb_img"})

for idx, image in enumerate(images):
    # print(image["src"])
    image_url = image["src"]
    if image_url.startswith("//"):  # if the var starts to "//"
        image_url = "https" + image_url

    # print(image_url)
    image_res = requests.get(image_url)  # Request to get url of image
    image_res.raise_for_status()  # Check the var [the url] is not error

    with open("movie{}.jpg".format(idx+1), "wb") as f:  # wb : img is not text but 바이넌?
        f.write(image_res.content)  # image_res.context = img

    if idx >= 4:  # Download up to top 5
        break
