from urllib.parse import urljoin

base = "http://example.com/html/a.html"

# base url과 url을 하나로 합친 URL형식으로 반환한다.
print(urljoin(base, "b.html"))
print(urljoin(base, "sub/c.html"))
print(urljoin(base, "../index.html"))
print(urljoin(base, "../img/hoge.png"))
print(urljoin(base, "../css/hoge.css"))

# url이 http://로 시작하면 합치지 않는다.
print(urljoin(base, "http://otherExample.com/wiki"))