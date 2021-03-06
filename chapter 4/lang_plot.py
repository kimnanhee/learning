import matplotlib.pyplot as plt
import pandas as pd
import json

# JSON 파일의 데이터 읽어오기
with open("./lang/freq.json", "r", encoding="utf-8") as fp:
    freq = json.load(fp)

# 언어마다 계산하기
lang_dic = {}
for i, lbl in enumerate(freq[0]["labels"]):
    fq = freq[0]["freqs"][i]
    if not (lbl in lang_dic):
        lang_dic[lbl] = fq
        continue
    for idx, v in enumerate(fq):
        lang_dic[lbl][idx] = (lang_dic[lbl][idx] + v) / 2

# Pandas의 DataFrame에 데이터 넣기
asclist = [[chr(n) for n in range(97, 97+26)]]
df = pd.DataFrame(lang_dic, index = asclist)

# 그래프 그리기
plt.style.use("ggplot")
df.plot(kind = "bar", subplots = True, ylim = (0, 0.15)) # 막대 그래프
plt.savefig("lang-plot-bar.png")
df.plot(kind = "line", subplots = True, ylim = (0, 0.15)) # 꺽은선 그래프
plt.savefig("lang-plot-line.png")