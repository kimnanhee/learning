import tensorflow as tf

# 플레이스 홀더 정의하기
a = tf.placeholder(tf.int32, [3])

# 배열의 모든 값을 2배하는 연산 정의하기
b = tf.constant(2)
x2_op = a * b

# 세션 시작하기
sess = tf.Session()

# 플레이스 홀더에 값을 넣고 실행하기
res1 = sess.run(x2_op, feed_dict={a:[1, 2, 3]})
res2 = sess.run(x2_op, feed_dict={a:[10, 20, 30]})
print(res1)
print(res2)