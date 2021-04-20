from PIL import Image
import numpy as np

# 이미지를 average hash로 변환하기
def average_hash(fname, size=16):
    img = Image.open(fname)
    img = img.convert('L') # 그레이스케일 변환
    img = img.resize((size, size), Image.ANTIALIAS) # 리사이즈
    pixel_data = img.getdata() # 픽셀 데이터 가져오기
    pixels = np.array(pixel_data) # numpy 배열로 변환
    pixels = pixels.reshape((size, size)) # 2차원 배열로 변환
    avg = pixels.mean() # 평균 구하기
    diff = 1 * (pixels > avg)
    return diff

# 이진 해시로 변환하기
def np2hash(ahash):
    bhash = []
    for nl in ahash.tolist():
        s1 = [str(i) for i in nl]
        s2 = "".join(s1)
        i = int(s2, 2) # 이진수를 정수로 변환
        bhash.append("%04x" % i)
    return "".join(bhash)

# Average Hash 출력하기
ahash = average_hash('apple.jpg')
print(ahash)
print(np2hash(ahash))