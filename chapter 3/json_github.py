import urllib.request as req
import os.path, random
import json

# json 다운로드
url = "https://api.github.com/repositories"
savename = "repo.json"
req.urlretrieve(url, savename)
# 저장한 json 파일이 있으면 읽어서 사용하기
# if not os.path.exists(savename):
    # req.urlretrieve(url, savename)

# json 파일 분석하기
s = open(savename, "r", encoding="utf-8").read()
items = json.loads(s)

# 출력하기
for item in items:
    print(item["name"], "-", item["owner"]["login"])