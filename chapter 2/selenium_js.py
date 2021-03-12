from selenium.webdriver import Firefox, FirefoxOptions

# 파이어폭스 실행
options = FirefoxOptions()
options.add_argument('-headless')
browser = Firefox(options=options)

browser.get("http://google.com")

r = browser.execute_script("return 100 + 50")
print(r)