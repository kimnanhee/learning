import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Okt
import urllib.request
import os, re, json, random

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

# 마르코프 체인 만들기
def make_dic(words):
    tmp = ["@"]
    dic = {}
    for word in words:
        tmp.append(word)
        if len(tmp) < 3: continue
        if len(tmp) > 3: tmp=tmp[1:]
        set_word3(dic, tmp)
        if word == ".":
            tmp = ["@"]
            continue
    return dic

# 딕셔너리에 단어 등록하기
def set_word3(dic, s3):
    w1, w2, w3 = s3
    if not w1 in dic: dic[w1] = {}
    if not w2 in dic[w1]: dic[w1][w2] = {}
    if not w3 in dic[w1][w2]: dic[w1][w2][w3] = 0
    dic[w1][w2][w3] += 1

# 문장 만들기
def make_sentence(dic):
    ret = []
    if not "@" in dic: return "no dict"
    top = dic["@"]
    w1 = word_choice(top)
    w2 = word_choice(top[w1])
    ret.append(w1)
    ret.append(w2)
    while True:
        w3 = word_choice(dic[w1][w2])
        ret.append(w3)
        if w3 == ".": break
        w1, w2 = w2, w3
    ret = "".join(ret)

    # 파이어폭스 실행
    options = ChromeOptions()
    options.add_argument("-headless")
    browser = Chrome()

    url_login = "https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=0&acr=1&acq=%EB%A7%9E%EC%B6%94&qdt=0&ie=utf8&query=%EB%A7%9E%EC%B6%A4%EB%B2%95%EA%B2%80%EC%82%AC%EA%B8%B0"
    browser.get(url_login)
    try:
        tag_textarea = browser.find_element_by_class_name("txt_gray")
        tag_textarea.click()
        pyperclip.copy(ret)
        time.sleep(1)
        tag_textarea.send_keys(Keys.CONTROL, 'a')
        tag_textarea.send_keys(Keys.CONTROL, 'v')

        tag_btn = browser.find_element_by_class_name("btn_check")
        tag_btn.click()

        time.sleep(2)

        tag_copy = browser.find_element_by_class_name("copy")
        tag_copy.click()
        data = pyperclip.paste()
    except:
        return "error"
    # 리턴
    return data

def word_choice(sel):
    keys = sel.keys()
    return random.choice(list(keys))

# 문장 읽어들이기
toji_file = "toji.txt"
dict_file = "markov_toji.json"
if not os.path.exists(dict_file):
    # 토지 텍스트 파일 읽어들이기
    fp = codecs.open("BEXX0003.txt", "r", encoding="utf-16")
    soup = BeautifulSoup(fp, "html.parser")
    body = soup.select_one("body > text")
    text = body.getText()
    text = text.replace("···", "")
    
    # 형태소 분석
    okt = Okt()
    malist = okt.pos(text, norm=True)
    words = []
    for word in malist:
        # 구두점 등은 대상에서 제외
        if not word[0] in ["Punctuation"]:
            words.append(word[0])
        if word[0] == ".":
            words.append(word[0])
    
    # 딕셔너리 생성
    dic = make_dic(words)
    json.dump(dic, open(dict_file, "w", encoding="utf-8"))

else:
    dic = json.load(open(dict_file, "r"))

# 문장 만들기
for i in range(3):
    s = make_sentence(dic)
    print(s)
    print("------------------")