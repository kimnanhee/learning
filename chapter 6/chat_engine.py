import codecs
from bs4 import BeautifulSoup
import urllib.request
from konlpy.tag import Okt
import os, re, json, random

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

dict_file = "chatbot_data.json"
dic = {}
okt = Okt()

# 딕셔너리에 단어 등록하기
def register_dic(words):
    global dic
    if len(words) == 0: return
    tmp = ["@"]
    for i in words:
        word = i[0]
        if word == "" or word == "\r\n" or word == "\n": continue
        tmp.append(word)
        if len(tmp) < 3: continue
        if len(tmp) > 3: tmp=tmp[1:]
        set_word3(dic, tmp)
        if word == "." or word == "?":
            tmp = ["@"]
            continue
    # 딕셔너리가 변경될 때마다 저장하기
    json.dump(dic, open(dict_file, "w", encoding="utf-8"))

# 딕셔너리에 글 등록하기
def set_word3(dic, s3):
    w1, w2, w3 = s3
    if not w1 in dic: dic[w1] = {}
    if not w2 in dic[w1]: dic[w1][w2] = {}
    if not w3 in dic[w1][w2]: dic[w1][w2][w3] = 0
    dic[w1][w2][w3] += 1

# 문장 만들기
def make_sentence(head):
    # print("make sentence head -", head)
    if not head in dic: return ""
    ret = []
    if head != "@": ret.append(head)
    top = dic[head]
    w1 = word_choice(top)
    w2 = word_choice(top[w1])
    ret.append(w1)
    ret.append(w2)
    while True:
        if w1 in dic and w2 in dic[w1]:
            w3 = word_choice(dic[w1][w2])
        else:
            w3 = ""
        ret.append(w3)
        if w3 == "." or w3 == "?" or w3 == "": break
        w1, w2 = w2, w3
    ret = "".join(ret)

    # 맞춤법 검사하기
    options = ChromeOptions()
    options.add_argument("headless")
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
        print("error")
    browser.close()
    return data

def word_choice(sel):
    keys = sel.keys()
    return random.choice(list(keys))

# 챗봇 응답 만들기
def make_reply(text):
    # 단어 학습시키기
    if not text[-1] in [".", "?"]: text += "."
    words = okt.pos(text)
    register_dic(words)
    # print("words -", words)
    # 사전에 단어가 있다면, 단어를 기반으로 문장 만들기
    for word in words:
        face = word[0]
        if face in dic: return make_sentence(face)
    return make_sentence("@")

# 딕셔너리가 있으면 읽어 들이기
if os.path.exists(dict_file):
    dic = json.load(open(dict_file, "r"))