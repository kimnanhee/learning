import codecs
from bs4 import BeautifulSoup
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
import numpy as np
import random, sys

fp = codecs.open("./BEXX0003.txt", "r", encoding="utf-16")
soup = BeautifulSoup(fp, "html.parser")
body = soup.select_one("body")
text = body.getText() + " "
print("코퍼스의 길이 :", len(text))

# 문자를 하나하나 읽어 들이고 ID 붙이기
chars = sorted(list(set(text)))
print("사용되고 있는 문자의 수 :", len(chars))
char_indices = dict((c, i) for i, c in enumerate(chars)) # 문자 -> ID
indices_char = dict((i, c) for i, c in enumerate(chars)) # ID -> 문자