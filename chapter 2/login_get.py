import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 아이디와 비밀번호
Username = "kimnanhee"
Password = "nanhee0225"

# 세선 시작하기
session = requests.session()

# 로그인하기
login_info = {
    "login" : Username,
    "password" : Password
}

url_login = "https://github.com/session"
res = session.post(url_login, data=login_info)
res.raise_for_status() # 오류가 발생하면 예외 발생