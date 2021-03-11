import requests

# 데이터 가져오기
r = requests.get("http://api.aoikujira.com/time/get.php")

# text 형식으로 데이터 추출하기
text = r.text
print(text)

# binary 형식으로 데이터 추출하기
bin = r.content
print(bin)