from bs4 import BeautifulSoup
import urllib.request

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# 다운로드
data = urllib.request.urlopen(url)

# 다운받은 데이터 분석하기
soup = BeautifulSoup(data, "html.parser")

# 메서드 추출하기
title = soup.find("title").string
wf = soup.find("wf").string
print(title)
print(wf)