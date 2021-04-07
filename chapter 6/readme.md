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

​	wiki_wakati : 

```python
from gensim.models import word2vec
model = word2vec.Word2Vec.load("wiki.model")
model.wv.most_similar(positive=["Python", "파이썬"])
model.mv.most_similar(positive=["왕자", "여성"], negative=["남성"])[0:5]
```



