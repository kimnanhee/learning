from bs4 import BeautifulSoup

html = """
<html><body>
    <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
    </ul>
</body></html>
"""

# html 분석하기
soup = BeautifulSoup(html, 'html.parser')

# 메서드 추출하기
links = soup.find_all('a')

# 링크 목록 출력하기
for link in links:
    href = link.attrs['href']
    text = link.string
    print(text, ">", href)