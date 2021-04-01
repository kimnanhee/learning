import pandas as pd
import numpy as np
import tensorflow as tf

# bmi csv 파일 읽어 들이기
csv = pd.read_csv("bmi.csv")

# 데이터 정규화
csv["height"] = csv["height"] / 200
csv["weight"] = csv["weight"] / 100