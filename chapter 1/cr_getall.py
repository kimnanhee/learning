from bs4 import BeautifulSoup
from urllib.request import *
from urllib.parse import *
from os import link, makedirs
import os.path, time, re

# 이미 처리한 파일인지 확인하기 위한 변수
proc_files = {}

def enum_links(html, base):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.select("link[rel='stylesheet']")
    links += soup.select("a[href]")
    result = []

    for a in links:
        href = a.attrs['href']
        url = urljoin(base, href)
        result.append(url)
    return result

# 파일을 다운받고 저장하는 함수ㄴ
def download_file(url):
    o = urlparse(url)
    savepath = "./" + o.netloc + o.path
    if re.search(r"/$", savepath):
        savepath += "index.html"

    savedir = os.path.dirname(savepath)

    if os.path.exists(savepath):
        return savepath
    
    # 다운받을 폴더 생성
    if not os.path.exists(savedir):
        print("mkdir=", savedir)
        makedirs(savedir)

    # 파일 다운받기
    try:
        print("download=", url)
        urlretrieve(url, savepath)
        time.sleep(1)
        return savepath
    except:
        print("download fail=", url)
        return None

# HTML을 분석하고 다운받는 함수
def analyze_html(url, root_url):
    savepath = download_file(url)
    if savepath is None: return
    if savepath in proc_files: return # 다운받았으면 실행하지 않음

    # 링크 추출
    proc_files[savepath] = True
    print("analyze_html=", url)

    html = open(savepath, "r", encoding="utf-8").read()
    links = enum_links(html, url)

    for link_url in links:
        if link_url.find(root_url) != 0:
            if not re.search(r".css$", link_url):
                continue
        if re.search(r".(html|htm)$", link_url):
            # 재귀적으로 HTML파일을 분석
            analyze_html(link_url, root_url)
            continue
        download_file(link_url)

if __name__ == "__main__":
    # URL에 있는 모든 것 다운받기
    url = "http://docs.python.org/3.8/library/"
    analyze_html(url, url)