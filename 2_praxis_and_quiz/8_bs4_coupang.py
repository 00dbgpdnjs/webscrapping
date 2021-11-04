# << bs4 활용편2 : 5개의 노트북 페이지에서 광고제품을 제외한  제품, 가격, 4.5 이상 평점, 100개 이상 평점수  가져오기 >>

import requests
import re
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50"}

for i in range(1, 6):
    # print("페이지 : ", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=&backgroundColor=".format(
        i)

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    # print(res.text) # To check whether the site'serve refuse me[my computer]

    # why do i use "re" : 모든 제품은 class로 search-product가 있고 광고 제품은 거기에 search-product__ad-badge도 있음 ; li 태그 중 class가 search-product로 시작하는 모든 제품을 찾아라
    items = soup.find_all("li", attrs={"class": re.compile("^search-product")})
    # print(items[0].find("div", attrs={"class":"name"}).get_text()) # Print first product name (= class가 name인 div태그의 텍스트[content])
    for item in items:

        # except to ad product
        # "item"에서 괄호 안의 두 조건을 만족하는(class가 ad-badge-text인 span태그) element
        ad_badge = item.find("span", attrs={"class": "ad-badge-text"})
        if ad_badge:
            # print("   <광고 상품 제외합니다>")
            continue  # Skip al; the codes below. Next index of "items"

        # 제품명 (= class가 name인 div태그의 텍스트[content])
        name = item.find("div", attrs={"class": "name"}).get_text()

        # Excluding Apple products.
        if "Apple" in name:
            # print("   <Apple 상품 제외합니다>")
            continue

        price = item.find("strong", attrs={"class": "price-value"}).get_text()
        # There may be no ratings.

        rate = item.find("em", attrs={"class": "rating"})
        if rate:
            rate = rate.get_text()
        else:
            # print("   <평점 없는 상품 제외합니다>")
            continue

        rate_cnt = item.find(
            "span", attrs={"class": "rating-total-count"})  # 몇 명이나 평점을 매겼는지
        if rate_cnt:
            # rate_cnt = rate_cnt.get_text()  # >> ex) (26)
            # rate_cnt = rate_cnt[1:-1]  # slicing : To remove bracket
            rate_cnt = rate_cnt.get_text()[1:-1]
            # print("리뷰 수", rate_cnt)
        else:
            # print("   <평점 수 없는 상품 제외합니다>")
            continue

        link = item.find("a", attrs={"class": "search-product-link"})["href"]

        # only products with a rating of 4.5 or higher  and  more than 100 reviews.
        if float(rate) >= 4.5 and int(rate_cnt) >= 100:
            # print(name, price, rate, rate_cnt)
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}점 ({rate_cnt}개)")
            print("바로가기 : {}".format("https://www.coupang.com" + link))
            print("-"*100)  # 제품마다 줄긋기
