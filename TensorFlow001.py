import tensorflow as tf

a = tf.Variable(5.0)

sess =  tf.Session()

print(sess.run(a))