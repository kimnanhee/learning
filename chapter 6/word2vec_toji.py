import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from gensim.models import word2vec

# utf-16 encoding으로 파일을 열고 글자를 출력하기
fp = codecs.open("BEXX0003.txt", "r", encoding="utf-16")
soup = BeautifulSoup(fp, "html.parser")
body = soup.select_one("body > text")
text = body.getText()

# 텍스트를 한 줄씩 처리하기
okt = Okt()
results = []
lines = text.split("\n")
for line in lines:
    # 형태소 분석하기 - 단어의 기본형 사용
    malist = okt.pos(line, norm=True, stem=True)
    r = []
    for word in malist:
        if not word[1] in ["Josa", "Emoi", "Punctuation"]:
            r.append(word[0])
    rl = (" ".join(r)).strip()
    results.append(rl)
    # print(rl)

# 파일로 출력하기
gubun_file = "toji.gubun"
with open(gubun_file, "w", encoding="utf-8") as fp:
    fp.write("\n".join(results))

# word2vec 모델 만들기
data = word2vec.LineSentence(gubun_file)
model = word2vec.Word2Vec(data, window=10, hs=1, min_count=2, sg=1)
model.save("toji.model")
print("ok")