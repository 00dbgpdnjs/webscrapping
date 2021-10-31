import requests
from bs4 import BeautifulSoup

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&oquery=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80&tqi=hUz9zwprvxZsseIUexGssssss4d-318723"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    # "흐림, 어제보다 00° 높아요" 구현
    cast = soup.find("p", attrs={"class":"summary"}).get_text()

    # "현재 00℃ (최저 00° / 최고 00°)" 구현
    curr_temp = soup.find("div", attrs={"class":"temperature_text"}).get_text().strip()
    min_temp = soup.find("span", attrs={"class":"lowest"}).get_text()
    max_temp = soup.find("span", attrs={"class":"highest"}).get_text()

    # "오전 강수확률 00% / 오후 강수확률 00%" 구현
    rain_rate = soup.find("span", attrs={"class":"weather_left"})
    mornig_rain_rate = rain_rate.get_text().strip()
    rain_rate = rain_rate.parent
    rain_rate = rain_rate.find_next_sibling("span")
    afternoon_rain_rate = rain_rate.find("span", attrs={"class":"weather_left"}).get_text().strip()

    # 미세먼지 (00㎍/m³) 좋음
    # 초미세먼지 (00㎍/m)³ 좋음
    dust = soup.find("ul", attrs={"class":"today_chart_list"})
    pm10 = dust.find_all("li")[0].get_text().strip()
    pm25 = dust.find_all("li")[1].get_text().strip()
    # pm25 = dust.find_all("li")[2].get_text().strip()

    print(cast)
    print("{} ({} / {})".format(curr_temp, min_temp, max_temp))
    print("강수확률 : {} / {}".format(mornig_rain_rate, afternoon_rain_rate))
    print()
    print(pm10) # 됐다가 안됐다 함...
    print(pm25)
    print()

# ...get_text().replace("도씨", ""): Replace 도씨 among text 
# p태그의 텍스트가 다른 태그로 각각 감싸져 있어도 모든 text를 가져올 수 있음. p태그가 상위태그
# ...get_text().strip(): Del unnecessary blank

# Work when main ; The func only runs when this project is executed directly, and does not run when called by another file.
if __name__ == "__main__": 
    scrape_weather()