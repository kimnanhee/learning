import pandas as pd

# 키, 몸무게, 유형 데이터 생성하기
thl = pd.DataFrame({
    "weight" : [80.0, 70.4, 65.5, 45.9, 51.2],
    "height" : [175, 180, 166, 152, 162],
    "gender" : ["f", "m", "m", "f", "m"]
})

# 키와 몸무게 정규화하기
# 최댓값과 최솟값 구하기
def norm(thl, key):
    c = thl[key]
    v_max = c.max()
    v_min = c.min()
    print(key, ":", v_min, v_max)
    thl[key] = (c-v_min) / (v_max-v_min)

norm(thl, "weight")
norm(thl, "height")
print(thl)