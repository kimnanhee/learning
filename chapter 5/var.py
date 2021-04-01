import tensorflow as tf
from tensorflow.python.ops.gen_state_ops import assign

# 상수 정의하기
a = tf.constant(120, name="a")
b = tf.constant(130, name="b")
c = tf.constant(140, name="c")

# 변수 정의하기
v = tf.Variable(0, name="v")

# 데이터 플로우 그래프 정의하기
calc_op = a + b + c
assign_op = tf.assign(v, calc_op)

# 세션 시작하기
sess = tf.Session()
res = sess.run(assign_op)
print(sess.run(v))