################################################################
#  Neural - 신경망 손글씨 이미지로 추론
#           MNIST Data Set 활용
#           입력층 뉴런 = 28 * 28 = 784개
#           출력층 뉴런 = 10개 -> 0 ~ 9까지의 숫자 구분
#           은닉층 2개 -> 임의로 정의
#            - 첫 번째 은닉층: 50개
#            - 두 번째 은닉층: 100개
################################################################
import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
import pickle
from dataset.mnist import load_mnist

def sigmoid(s):
    return 1 / (1 + np.exp(-s))


def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y


def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test


def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network


def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y


x, t = get_data()
network = init_network()

accuracy_cnt = 0
batch_size = 100  # 배치 크기

for i in range(0, len(x), batch_size):
    x_batch = x[i:i++batch_size]         # x[0:100], [100:200], [200:300]....
    y_batch = predict(network, x_batch)
    p = np.argmax(y_batch, axis=1)
    #     0   1   2
    # 0 [0.1 0.8 0.1]   --> 최대값을 가지는 index: 1
    # 1 [0.3 0.1 0.6]   --> 최대값을 가지는 index: 2
    # 2 [0.2 0.5 0.3]   --> 최대값을 가지는 index: 1
    # 3 [0.8 0.1 0.1]   --> 최대값을 가지는 index: 0
    # p 의 값: [1 2 1 0]
    accuracy_cnt += np.sum(p == t[i:i+batch_size])

"""
for i in range(len(x)):
    y = predict(network, x[i])
    p = np.argmax(y)
    if p == t[i]:
        accuracy_cnt += 1
"""
print("Accuracy:" + str(float(accuracy_cnt) / len(x)))