## Chapter 2

### 2-1

​	requests_test : "requests" 라이브러리를 사용해서 시간 확인 웹에서 데이터 가져오기

​	requests_png : "requests" 라이브러리를 사용해서 바이너리 데이터인 이미지를 받아 저장하기



### 2-2

​	Selenium + Firefox 실행 환경

​	selenium_capture : 네이버의 메인 페이지를 캡져해서 저장하기

​	selenium_login : 네이버에 로그인하고 쇼핑 페이지의 구매 목록 가져오기

​	selenium_js : 자바스크립트 실행한 뒤 결과를 추출하기



### 2-3

​	api_weather : OpenWeatherMap의 웹 API를 사용해서 날씨 정보 가져오기



### 2-4

​	everyday_dollar : 네이버 금융에서 환율을 가져오고, 이름이 날짜인 텍스트 파일을 만들어서 저장하기, pyinstaller로 실행 파일 만들기



### 2-5

​	Scrapy 사용

​	book1 : scapy를 사용해서 위키 북스의 도서 목록 링크를 추출하기

​	book2 : scrapy를 사용해서 위키 북스의 도서 목록의 링크와 텍스트 추출하기, Json 파일을 만들어서 데이터 저장하기

```
scrapy shell

fetch("http://wikibook.co.kr/list/)

response.css("title::text").extract_first()
response.css("h4::text").extract()

quit()
```



### 2-6

​	book3 : scrapy를 사용해서 위키 북스의 도서 목록의 표지 이미지 링크 추출하기

​	book4 : scrapy를 사용해서 위키 북스의 도서 목록의 표시 이미지 저장하기