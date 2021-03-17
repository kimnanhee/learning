# 파일 이름과 데이터
fname = "a.bin"
data = 100

# 쓰기
with open(fname, "wb") as f:
    f.write(bytearray([data]))