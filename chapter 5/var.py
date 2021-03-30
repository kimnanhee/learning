import tensorflow as tf

# 상수 정의하기
a = tf.constant(120, name="a")
b = tf.constant(130, name="b")
c = tf.constant(140, name="c")

# 변수 정의하기
v = tf.Variable(0, name="v")

# 데이터 플로우 그래프 정의하기
v = tf.add_n([a, b, c])

# 결과 출력하기
tf.print(v)