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

​	wiki_wakati : 

```python
from gensim.models import word2vec
model = word2vec.Word2Vec.load("wiki.model")
model.wv.most_similar(positive=["Python", "파이썬"])
model.mv.most_similar(positive=["왕자", "여성"], negative=["남성"])[0:5]
```



### 베이즈 정리(Bayes' theorem)

조건부 확률과 관련된 이론, P(B|A) = P(A|B) * P(B) / P(A)

단순한 출현율 = 단어의 출현 횟수 / 카테고리 전체 단어의 수



### 6-3

​	bayes : 베이지안 필터를 구현한 BayesianFilter 클래스 생성하기

​	bayes_test : BayesianFilter 클래스의 fit 메서드로 텍스트를 학습시키고, 판정 결과를 출력하기

