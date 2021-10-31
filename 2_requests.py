# requests library : 웹 페이지 정보 가져오기 ; html 문서 정보 가져오기
# requests : Read web page(html) on static page cf) selenium : web page auto on dynamic page
# Both can scrap[extract the data you want] to BeautifulSoup 
# $ pip install requests

import requests

# Put url[what you want] in round brakets
res = requests.get("http://google.com")  # ❗ KEY CODE ❗
# If 200, success. If 403, no authority to access.
# print("응답코드 :", res.status_code)

# if res.status_code == requests.codes.ok: # ok = 200
# 	print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

# Instead the for statement just above / If there is problem, give the error as ending this program [ending running this file]
res.raise_for_status()  # ❗ KEY CODE ❗
# print("웹 스크래핑을 진행합니다")

print(len(res.text))
print(res.text)  # >> google html

# Makes soup obj's text  html file to check if there's text what you want. If not, put useragent or use selenium
with open("mygoogle.html", "w", encoding="utf8") as f:  # (filename to be made)
    f.write(res.text)  # where.write(what)
