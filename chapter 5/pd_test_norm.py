import pandas as pd

# 키, 몸무게, 유형 데이터 생성하기
thl = pd.DataFrame({
    "weight" : [80.0, 70.4, 65.5, 45.9, 51.2],
    "height" : [175, 180, 166, 152, 162],
    "gender" : ["f", "m", "m", "f", "m"]
})

def norm(thl, key, value):
    c = thl[key]
    thl[key] = c / value

# thl["weight"] = [i / 100 for i in thl["weight"]]
# thl["height"] = [i / 200 for i in thl["height"]]
norm(thl, "weight", 100)
norm(thl, "height", 200)
print(thl)