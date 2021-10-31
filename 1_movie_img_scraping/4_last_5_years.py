# << web scraping program : Save top 5 movies's thumbnail in the last 5 years on Daum >>

import requests
from bs4 import BeautifulSoup

for year in range(2016, 2021):  # In the last 5 years
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(
        year)
    # This link : site to work
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class": "thumb_img"})

    for idx, image in enumerate(images):  # for .. break : top5
        # print(image["src"])
        image_url = image["src"]
        if image_url.startswith("//"):  # if the var starts to "//"
            image_url = "https" + image_url

        # print(image_url)
        image_res = requests.get(image_url)  # Request to get url of image
        image_res.raise_for_status()  # Check the var [the url] is not error

        # wb : img is not text but 바이넌? / idx+1 format 만 하면 년마다 파일명이 중복됨 ; 2016년 for문에서 movie1~5.jpg 파일이 생성되고, 2017년 for문에서도 movie1~5.jpg 파일이 생성됨
        with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f:
            f.write(image_res.content)  # image_res.context = img

        if idx >= 4:  # Download up to top 5
            break
