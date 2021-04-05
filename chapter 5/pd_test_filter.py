import pandas as pd

# 키, 몸무게, 유형 데이터 생성하기
thl = pd.DataFrame({
    "weight" : [80.0, 70.4, 65.5, 45.9, 51.2],
    "height" : [175, 180, 166, 152, 162],
    "gender" : ["f", "m", "m", "f", "m"]
})

print("-- 키가 165 이상인 것")
print(thl[thl.height >= 165])
print("-- 성이 f 인 것")
print(thl[thl.gender == "f"])