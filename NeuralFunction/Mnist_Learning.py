################################################################
#  Neural - 신경망 손글씨 이미지 데이터 인식
#           MNIST Data Set 활용
#           /data/mnist.py 통해 세팅 가능
################################################################
import os
import sys

sys.path.append(os.pardir)
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)