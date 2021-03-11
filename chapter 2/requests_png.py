import requests

# 데이터 가져오기
r = requests.get("http://wikibook.co.kr/wikibook.png")

# binary 형식으로 데이터 저장하기
with open("test.png", "wb") as f:
    f.write(r.content)

print("saved")