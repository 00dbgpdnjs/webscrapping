from selenium import webdriver

# exe가 같은 경로에 있다면 "./chromedriver.exe" 생략가능. 아니라면 "c:/downloads/chromedriver.exe" 이런식으로
# Create chromewebdriver obj / Open chrome browser
# "browser"[exe] controls chrome
browser = webdriver.Chrome() # ❗❗ KEY CODE ❗❗
browser.get("http://naver.com")  # Move to [Open] the url in "brower"

# < How to click login btn >
elem = browser.find_element_by_class_name("link_login")
# print(elem) # >> webelement obj
elem.click()  # My computer clicks login btn

# browser.close() # Close only curr opened tap
browser.quit()  # Turn off browser

# -----------------------------------------------------------
# browser.back() # Go back
# browser.forward() # Go forward
# browser.refresh() # Refresh web
# N.B. : Whenver the page is switched and you'll use "elem" var again, the "elem" must be reset[re-defined].
# N.B. : 컴퓨터의 컨트롤 속도와  컨트롤에 의한 작동 속도의 차이 때문에 에러가 뜰 수 있다. 기다리다가 꺼지면 다시열기
# error msg : is not clickable at point [바로 클릭 할 수 있는 위치에  없다] -> 클릭되는 한에서 더 상위 엘레먼트 가져오기 (xpath의 경우 "/" 하나씩 지워가기)
