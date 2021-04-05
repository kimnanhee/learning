import numpy as np

# 10개의 flaot32 자료형 데이터 생성
v = np.zeros(10, dtype=np.float32)
print(v)

# 연속된 10개의 uint64 자료형 데이터 생성
v = np.arange(10, dtype=np.uint64)
print(v)

# v 값을 3배
v *= 3
print(v)

# v 평균
print(v.mean())