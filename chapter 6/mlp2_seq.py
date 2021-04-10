import os, glob, json

root_dir = "./newstext"
dic_file = root_dir + "/word_dic.json"
data_file = root_dir + "/data.json"
data_file_min = root_dir + "/data_mini.json"

# 어구를 자르고 ID로 변환하기
word_dic = {"_MAX" : 0}

def text_to_ids(text):
    text = text.strip()
    words = text.split(" ")
    result = []
    for word in words:
        word = word.strip()
        if word == "": continue
        if not word in word_dic:
            wid = word_dic[word] = word_dic["_MAX"]
            word_dic["_MAX"] += 1
            print(wid, word)
        else:
            wid = word_dic[word]
        result.append(wid)
    return result

# 파일을 읽고 고정 길이의 배열 리턴하기
def file_to_ids(fname):
    with open(fname, "r") as f:
        text = f.read()
        return text_to_ids(text)

# 딕셔너리의 단어 모두 등록하기
def register_dic():
    files = glob.glob(root_dir + "/*/*.gubun", recursive=True)
    for file in files:
        file_to_ids(file)

# 파일 내부의 단어 세기
def count_file_freq(fname):
    cnt = [0 for n in range(word_dic["_MAX"])]
    with open(fname, "r") as f:
        text = f.read().strip()
        ids = text_to_ids(text)
        for word in ids:
            cnt[word] += 1
    return cnt

# 카테고리마다 파일 읽어 들이기
def count_freq(limit = 0):
    x = []
    y = []
    max_words = word_dic["_MAX"]
    cat_names = []
    for cat in os.listdir(root_dir):
        cat_dir = root_dir + "/" + cat
        if not os.path.isdir(cat_dir): continue
        cat_idx = len(cat_names)
        cat_names.append(cat)
        files = glob.glob(cat_dir + "/*.gubun")
        i = 0
        for path in files:
            print(path)
            cnt = count_file_freq(path)
            x.append(cnt)
            y.append(cat_idx)
            if limit > 0:
                if i > limit: break
                i += 1
    return x, y

# 단어 딕셔너리 만들기
if os.path.exists(dic_file):
    word_dic = json.load(open(dic_file))
else:
    register_dic()
    json.dump(word_dic, open(dic_file), "w")

# 벡터를 파일로 출력하기
# 테스트 용 데이터 만들기
x, y = count_freq(20)
json.dump({"x" : x, "y" : y}, open(data_file_min, "w"))

# 전체 데이터 만들기
x, y = count_freq()
json.dump({"x" : x, "y" : y}, open(data_file, "w"))
print("ok")