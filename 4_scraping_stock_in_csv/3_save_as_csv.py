# << 목표1. 네이버 코스피 시가 총액 순위 정보를 스크래핑 >>
# << 목표2. 웹 스크래핑을 이용해서 가져온 데이터[네이버 금융]를 csv 파일로 저장 >>

# << Save this file as a csv file. Open it on excel >>

import csv
import requests  # csv module
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
# "w" : 써지는 방식 / 엑셀로 열었는데 한글이 깨지면 utf8 대신 utf-8-sig로 바꾸기 (signature) / newline="": 사이사이에 한 줄 공백이 디폴트로 들어가는 것을 공백[""]처리함[없앰]
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)  # ❗❗ KEY CODE ❗❗

for page in range(1, 5):  # page1 ~ page4 : total 200 companies
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    # table 태그이면서 class가 type_2인 엘리먼트를 찾고 그 중 tbody 태그를 찾고 그 중 모든 tr을 찾아라
    # data_rows : Each row[tr; company's info] is as a list.
    data_rows = soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all(
        "tr")
    for row in data_rows:
        # (The subtag of tr["row"],)  td : numerical info about 현재가, 거래량, PER etc.
        columns = row.find_all("td")
        # To skip meaningless data like the td for sperator[division line]. cuz 의미 없는 tr은 td를 하나 이하만 갖고 있음 각 수치 정보 td가 없으므로
        if len(columns) <= 1:
            # Don't execute the codes below and move on to the next idx of the for statement.
            continue
        # 한 줄 for 문 : columns를 column으로 하나씩 가져와서 column.get_text()를 가져옴
        # "data" : Text info of each column[td]
        # strip(): Delete /n or /t
        data = [column.get_text().strip() for column in columns]
        # before adding the code just above and strip() >> [''] : sperator[division line]을 위한 비어있는 줄,  /n/t : 데이터[텍스트]에 불필요한 줄바꿈과 탭이 포함됨
        # print(data)
        writer.writerow(data)  # ❗❗ KEY CODE ❗❗
