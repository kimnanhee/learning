## Chapter 6

### 6-1

​	konlpy_basic : Okt 형태소 분석기를 사용해서 문장에 형태소를 분석해서 출력하기

​	toji_count : 국립국어원에서 다운받은 "토지" 데이터에서 많이 사용된 명사 50개 출력하기

​	word2vec_toji : Word2Vec를 사용해서 분석한 형태소를 읽어 들이고, 모델을 생성하기

```python
# 땅과 가까운 단어 출력하기
from gensim.models import word2vec
model = word2vec.Word2Vec.load("toji.model") 
model.wv.most_similar(positive=["땅"])
```



### 6-2

​	wiki_wakati : 위키피디아 데이터의 형태소를 분석하고 .gubun 파일에 저장하기. 약 12시간 소요 - 23400000 line

​	wiki_mkdic : .gubun 파일로 모델을 생성하기

```python
model = word2vec.Word2Vec.load("wiki.model")
model.wv.most_similar(positive=["Python", "파이썬"])
model.wv.most_similar(positive=["왕자", "여성"], negative=["남성"])[0:5]
```



### 베이즈 정리(Bayes' theorem)

조건부 확률과 관련된 이론, P(B|A) = P(A|B) * P(B) / P(A)

단순한 출현율 = 단어의 출현 횟수 / 카테고리 전체 단어의 수



### 6-3

​	bayes : 베이지안 필터를 구현한 BayesianFilter 클래스 생성하기

​	bayes_test : BayesianFilter 클래스의 fit 메서드로 텍스트를 학습시키고, 판정 결과를 출력하기



### 다층 퍼셉트론(Multi Layer Perceptron, MLP)

입력층과 출력층 사이에 각각 전체 결합하는 은닉층을 넣은 뉴럴 네트워크



### 6-4

​	mlp2_seq : 텍스트를 숫자 벡터로 변환하기. 학습에 사용할 데이터를 JSON 형식으로 저장하기

​	mlp3_classify : JSON 형식의 데이터를 읽고, Keras로 MLP 모델을 구축해서 테스트하기



### 6-5

​	lev_distance : 레벤슈타인 거리를 계산해서 문자열 사이의 거리 출력하기

​	ngram_test : N-gram으로 문장의 유사도를 구해서 출력하기



### 6-6

​	markov : 토지의 문장을 분석해서 json 형식의 파일에 저장하기. 마르코프 체인을 사용해서 문장을 생성해서 출력하기