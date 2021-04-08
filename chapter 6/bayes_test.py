from bayes import BayesianFilter
bf = BayesianFilter()

# 텍스트 학습
bf.fit("파격 세일 오늘까지 할인", "광고")
bf.fit("현대 백화점 세일", "광고")
bf.fit("쿠폰 선물 & 무료 배송", "광고")
bf.fit("인기 상품 최대 할인", "광고")

bf.fit("오늘 아침 회의가 있습니다", "중요")
bf.fit("오늘 일정 확인", "중요")
bf.fit("프로젝트 진행 상황 보고", "중요")
bf.fit("오늘 일정이 없습니다", "중요")

pre, scorelist = bf.predict("재고 정리 할인, 로켓 배송")
print("결과 :", pre)
print(scorelist)