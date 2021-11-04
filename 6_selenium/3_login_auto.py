# 활용1. Log in on Naver auto.

import time
from selenium import webdriver

browser = webdriver.Chrome()

# 1. Move on to [Open] Naver
browser.get("http://naver.com")

# 2. Click login btn
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. Put in id and pw
browser.find_element_by_id("id").send_keys("your_id")
browser.find_element_by_id("pw").send_keys("your_pw")

# 4. Click login btn
browser.find_element_by_id("log.login").click()

# In case of the msg, "Getting Default Adapter failed" cuz computer is slower than the speed to be controled
time.sleep(3)

# 5. Re-enter id cuz failing to log in
browser.find_element_by_id("id").clear()  # Delete value
# Without the code just above, Pre-data will be put in together.
browser.find_element_by_id("id").send_keys("your_real_id")

# 6. Print html (Provided[On the assumption ; Under the presumption ; Assuming] you were successful with logging in )
print(browser.page_source)  # page_source : Print all html

# 7. End browser
browser.close()
