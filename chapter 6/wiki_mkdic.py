from gensim.models import word2vec
data = word2vec.Text8Corpus("wiki.gubun")
model = word2vec.Word2Vec(data)
model.save("wiki.model")
print("ok")