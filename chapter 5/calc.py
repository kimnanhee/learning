# TensorFlow 추출하기
import tensorflow as tf

# 상수 정의
a = tf.constant(1234)
b = tf.constant(5000)

# 계산 정의
add_op = a + b

# 결과 출력하기
tf.print(add_op)