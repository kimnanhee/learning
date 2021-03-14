import requests
import json

# OpenWeathre의 API 키
apikey = ""

# 날씨를 확인할 도시
cities = ["Seoul,KR", "Tokyo,JP", "New York,US"]

# API 지정
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

# 캘빈 온도를 섭시 온도로 변환하는 함수
k2c = lambda k: k - 273.15

# 각 도시의 날찌 정보 출력하기
for name in cities:
    # url 구성하기
    url = api.format(city=name, key=apikey)

    # api에 요청을 보내 데이터 가져오기
    r = requests.get(url)

    # 데이터를 json형식으로 변환하기
    data = json.loads(r.text)

    # 결과 출력하기
    print("도시 =", data["name"])
    print("| 날씨 =", data["weather"][0]["description"])
    print("| 최저 기온 =", round(k2c(data["main"]["temp_min"]), 2), "°C")
    print("| 최고 기온 =", round(k2c(data["main"]["temp_max"]), 2), "°C")
    print("| 습도 =", data["main"]["humidity"], "%")
    print("| 기압 =", data["main"]["pressure"])
    print("| 풍향 =", data["wind"]["deg"])
    print("| 풍속 =", data["wind"]["speed"], "m/s")
    print("")