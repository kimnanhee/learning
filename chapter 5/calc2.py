# TensorFlow 추출하기
import tensorflow as tf

# 상수 정의
a = tf.constant(2)
b = tf.constant(3)
c = tf.constant(4)

# 계산 정의
calc1_op = a + b * c
calc2_op = (a + b) * c

# 결과 출력하기
print(calc1_op)
print(calc2_op)