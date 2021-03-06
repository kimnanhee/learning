from bs4 import BeautifulSoup
import urllib.request as req
import os.path

# XML 다운로드
url = "https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename = "forecast.xml"
req.urlretrieve(url, savename)
# 저장한 XML 파일이 있으면 읽어서 사용하기
# if not os.path.exists(savename):
#   req.urlretrieve(url, savename)

# BeautifulSoup로 분석하기
xml = open(savename, "r", encoding="utf-8").read()
soup = BeautifulSoup(xml, "html.parser")

info = {}
for location in soup.find_all("location"):
    name = location.find("city").string
    weather = location.find("wf").string
    if not (weather in info):
        info[weather] = []
    info[weather].append(name)
 
# 각 지역의 날씨를 구분해서 출력하기
for weather in info.keys():
    print("-", weather)
    for name in info[weather]:
        print("| ", name)