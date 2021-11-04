# 서버는 헤더 중 useragent를 보고 어떤 페이지를 보여줄지, 사람인지 확인
# - 웹사이트는 접속하는 사용자들의 (hearder) 정보를 알 수 있음. 브라우저가  내가 웹사이트에 접속할 때 주는 헤더정보에 따라서  사이트가 얘는 스마트폰이네 하면서 모바일용 페이지를 보여줌.
# - 그런데 사람이 아닌 웹크롤링이나 웹스크래핑을 하는 컴퓨터가 접속했을 때 사이트는 접속을 차단할 수 있음 (정보를 뺏길 수 있는 등의 이유로) (403 같은 응답코드를 주고 접속 차단 or 무한대기) -> user agent로 해결

# Search "(What is my) user agent"
# 브라우저 마다 user agent가 다름. 서버는 user agent를 확인해서 정보를 다르게 보여줄 수 있음
# "User-Agent에 user agent를 주고 requests.get 함수에서 headers에 넣기

import requests

url = "http://nadocoding.tistory.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50"}

res = requests.get(url)  # "티스토리" 사이트는 UserAgent를 변경하지 않아도 정상적으로 html 을 받아옴
# res = requests.get(url, headers=headers) # ❗ KEY CODE ❗ / 나머지는 2_requests.py와 같음 / headers로 user agent를 주면 직접 크롬에서 접속했을 때와 동일한 결과를 받아옴
res.raise_for_status()  # Refer to 2_requests.py

with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)
