# 기상청에서 기상 정보 가져오기
import urllib.request
import urllib.parse

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# 매개변수를 URL 인코딩
values = {
    'stnId' : '108' # 전국에 해당하는 지역 번호
}
params = urllib.parse.urlencode(values)

# 요청할 url 생성
url = API + '?' + params
print("url = ", url)

# 다운로드
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)