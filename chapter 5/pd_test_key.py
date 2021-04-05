import pandas as pd

# 키, 몸무게, 유형 데이터 생성하기
thl = pd.DataFrame({
    "weight" : [80.0, 70.4, 65.5, 45.9, 51.2],
    "height" : [175, 180, 166, 152, 162],
    "type" : ["f", "n", "n", "t", "t"]
})

# 몸무게 목록 추출하기
print("몸무게")
print(thl["weight"])

# 몸무게와 키 목록 추출하기
print("\n몸무게와 키")
print(thl[["weight", "height"]])