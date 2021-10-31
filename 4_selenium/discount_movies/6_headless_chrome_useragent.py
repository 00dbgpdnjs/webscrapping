# N.B. When headless chrome if the user agent is not changed[designated], the user agent info will be changed [blown away]), so the server may block access of computer.
# solution : Change[Designate] user-agent
# Unlike bs4, selenium work with my useragent auto

# < Print my useragent before and after changing[designating] my usergent  to check the N.B. >

from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36") # ❗❗ KEY CODE ❗❗ How to change[designate] useragent

browser = webdriver.Chrome(options=options) 
# browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

# My User Agent is:
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) 
# AppleWebKit/537.36 (KHTML, like Gecko) 
# Chrome/95.0.4638.54 Safari/537.36

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text) 
# >> changed useragent (before options.add_argument("user-agent=")) 
# >> right useragent (after it)

browser.quit()