import re
import requests
from bs4 import BeautifulSoup

def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50"}

    res = requests.get(url, headers=headers)
    res.raise_for_status()    

    soup = BeautifulSoup(res.text, "lxml")
    return soup

def print_news(index, title, link):
    print("{}. {}".format(index+1, title))
    print("   (링크 : {}".format(link))

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&oquery=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80&tqi=hUz9zwprvxZsseIUexGssssss4d-318723"
    soup = create_soup(url)

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

def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=3)
    for index, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        print_news(index, title, link)
    print()

def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3)
    for index, news in enumerate(news_list):
        # < Each article[li/"news"] has an article with and without an image. The former has a title on the second "a" tag after the 1st "a" tag with the image. And the latter has a title on the first tag. >
        a_idx = 0
        img = news.find("img")
        if img:
            a_idx = 1

        a_tag = news.find_all("a")[a_idx]
        title = a_tag.get_text().strip()
        link = a_tag["href"]
        print_news(index, title, link)
    print()

def scrape_english():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    # re.compile("^conv_kor_t") : conv_kor_t 로 시작함
    # Why re : 한글 지문과 영어 지문이 각각 4문장씩 있다면 첫 문장의 id가 conv_kor_t2로 시작해서 conv_kor_t5으로 끝남 (id 중복 가능?? 한글 지문과 영어 지문의 문장끼리 id가 같음...) 
    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})

    print("(영어지문)")
    # Why slicing[:] : Since the site has Korean fingerprints above, if a total of 8 sentences, the index of English fingerprints is 4 to 7.
    # Why is "//", not "/"? : If the total number of sentences rarely is odd, get the quotient (integer).
    for sentence in sentences[len(sentences)//2:]: 
        print(sentence.get_text().strip())
    print()

    print("(한글 지문)")
    for sentence in sentences[:len(sentences)//2]:
        print(sentence.get_text().strip())
    print()

# Work when main ; The func only runs when this project is executed directly, and does not run when called by another file.
if __name__ == "__main__": 
    scrape_weather()
    scrape_headline_news()
    scrape_it_news()
    scrape_english()