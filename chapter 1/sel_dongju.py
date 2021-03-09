from bs4 import BeautifulSoup
import urllib.request

url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"

# 다운로드
data = urllib.request.urlopen(url)

# 다운받은 데이터 분석하기
soup = BeautifulSoup(data, "html.parser")

 
# copy > copy selector
list = soup.select("#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > ul > li")

for i in list:
    name = i.string
    print("-", name)