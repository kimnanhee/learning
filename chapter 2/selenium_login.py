from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

ID = "kim-nan-hee"
PASS = "nanhee040225!"

# 파이어폭스 실행
options = ChromeOptions()
options.add_argument("-headless")
browser = Chrome()

url_login = "https://nid.naver.com/nidlogin.login"
browser.get(url_login)
print("로그인 페이지에 접근합니다.")

# 아이디와 비밀번호 입력
try:
    tag_id = browser.find_element_by_name("id")

    tag_pw = browser.find_element_by_name("pw")
    tag_id.clear()
    tag_pw.clear()

    tag_id.click()
    pyperclip.copy(ID)
    tag_id.send_keys(Keys.CONTROL, 'v')

    tag_pw.click()
    pyperclip.copy(PASS)
    tag_pw.send_keys(Keys.CONTROL, 'v')

    login_btn = browser.find_element_by_id("log.login")
    login_btn.click()
    print("로그인 버튼을 클릭합니다.")
    time.sleep(2)

except:
    pass

# 쇼핑 페이지의 데이터 가져오기
url_shop = "https://order.pay.naver.com/home?tabMenu=SHOPPING"
browser.get(url_shop)

time.sleep(2)

# 쇼핑 목록 출력
products = browser.find_elements_by_class_name("goods")
for product in products:
    print("-", product.find_element_by_class_name("name").text)