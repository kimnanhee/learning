from bs4 import BeautifulSoup
import urllib.request

url = "https://finance.naver.com/marketindex/"

# 다운로드
data = urllib.request.urlopen(url)

# 다운받은 데이터 분석하기
soup = BeautifulSoup(data, "html.parser")

# 메서드 추출하기
price = soup.select_one("div.head_info > span.value").string
print("usd/krw =", price)