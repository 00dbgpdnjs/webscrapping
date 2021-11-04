from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("http://naver.com") 

# << 다양한 방법(class(전 파일), id, xpath, tag 등)으로 컨트롤[click, write etc] 할 element 가져오기 >>

# < 1. Get elem of search bar by id >
# elem = browser.find_element_by_id("query")
# # print(elem)
# # Shen[Write][=!Search] "나도코딩" in search bar
# elem.send_keys("나도코딩")
# elem.send_keys(Keys.ENTER)  # Send[Click] enter key ;


# < 2. Get all href[link] of elem by "a" tag >
# elem = browser.find_element_by_tag_name("a")
# print(elem)

# elem = browser.find_elements_by_tag_name("a")
# print(elem)
# for e in elem:
#     print(e.get_attribute("href"))


# < 3. Get elem by namd and xpath >
browser.get("http://daum.net")  # Move on to the site wherever
elem = browser.find_element_by_name("q")
# print(elem)
elem.send_keys("나도코딩")
# elem.send_keys(Keys.ENTER)
elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]") # Instead of "Keys.ENTER"[computer press enter key on search-bar] just above, get search btn by using xpath
# How to get xpath of search btn : Find its (button) element and copy its xpath
# print(elem)
elem.click()

browser.quit()