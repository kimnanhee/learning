from bs4 import BeautifulSoup
import requests
from chat_engine import make_reply

header = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'} # 안티 크롤링
news_list = [
    "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=100", # 정치
    "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=101", # 경제
    "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=102", # 사회
    "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=103", # 생활 / 문화
    "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=105", # IT / 과학
    "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=110" # 오피니언
]
column_list = "https://news.naver.com/main/opinion/todayColumn.nhn?date=" # 20210416 형식으로 date에 값 대입
type06_list = ["type06_headline", "type06"]
links = []
column_links = []

for news in news_list:
    req =  requests.get(news, headers=header)
    soup = BeautifulSoup(req.content, 'html.parser', from_encoding='utf-8')

    for type06 in type06_list:
        content_list = soup.find("ul", class_=type06)
        dt_list = content_list.find_all("dt")
        for dt in dt_list:
            arr = dt.find_all("a")
            for inja in arr:
                links.append(inja["href"])

for date in range(20210418):
    req = requests.get(column_list+str(date), headers=header)
    soup = BeautifulSoup(req.content, 'html.parser', from_encoding='utf-8')
    
    content_list = soup.find("ul", class_="todaycolumn_list")
    strong_list = content_list.find_all(class_="todaycolumn_headline")
    for strong in strong_list:
        arr = strong.find_all("a")
        for inja in arr:
            column_links.append(inja["href"])

print(links)
print(len(links))
print(column_links)
print(len(column_links))

with open("../nesw.txt", "w", encoding="utf-8") as fp:
    for number, link in enumerate(links):
        print(number, "----------------------------------------")
        req =  requests.get(link, headers=header)
        soup = BeautifulSoup(req.content, 'html.parser', from_encoding='utf-8')
        try:
            text = soup.find("div", class_="_article_body_contents").get_text()
            print(text)
            fp.write(text)
            make_reply(text)
        except:
            pass

    for number, link in enumerate(column_links):
        print(number, "----------------------------------------")
        req =  requests.get(link, headers=header)
        soup = BeautifulSoup(req.content, 'html.parser', from_encoding='utf-8')
        try:
            text = soup.find("div", class_="_article_body_contents").get_text()
            print(text)
            fp.write(text)
            make_reply(text)
        except:
            pass