from selenium.webdriver import Firefox, FirefoxOptions

ID = "kim-nan-hee"
PASS = "nanhee040225!"

# 파이어폭스 실행
options = FirefoxOptions()
options.add_argument("-headless")
browser = Firefox(options=options)

url_login = "https://nid.naver.com/nidlogin.login"
browser.get(url_login)
print("로그인 페이지에 접근합니다.")

# 아이디와 비밀번호 입력
e = browser.find_element_by_name("id")
e.clear()
e.send_keys(ID)
e = browser.find_element_by_name("pw")
e.clear()
e.send_keys(PASS)

form = browser.find_element_by_css_selector("input.btn_global[type=submit]")
form.submit()
print("로그인 버튼을 클릭합니다.")

# 쇼핑 페이지의 데이터 가져오기
url_shop = "https://order.pay.naver.com/home?tabMenu=SHOPPING"
browser.get(url_shop)

# 쇼핑 목록 출력
products = browser.find_element_by_id("_listContentArea")
print(products)
for product in products:
    print("-", product.text)