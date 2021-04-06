from konlpy.tag import Okt
okt = Okt()
malist = okt.pos("오늘은 자습 시간에 공부를 할 것이다.", norm=True, stem=True)
print(malist)