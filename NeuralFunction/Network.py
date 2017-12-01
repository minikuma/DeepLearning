################################################################
#  Perceptron - 인공신경망모델링 3층 신경망
#               3층 신경망 구현
#               A = XW + B  -> 벡터의 내적
#               A = (a1, a2, a3), X = (x1, x2), B = (b1, b2, b3)
#               W = [ w11, w21, w31]
#                     w12, w22, w32
################################################################
import numpy as np

# Sigmoid Function
def sigmoid(s):
    return 1 / (1 + np.exp(-s))

# 항등함수
def identify_function(x):
    return x

# 가중치와 편향 초기화 및 값 저장
def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])   # 2차원 배열
    network['b1'] = np.array([0.1, 0.2, 0.3])                      # 1차원 배열
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]]) # 2차원 배열
    network['b2'] = np.array([0.1, 0.2])                           # 1차원 배열
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])             # 2차원 배열
    network['b3'] = np.array([0.1, 0.2])                           # 1차원 배열

    return network


def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1    # x와 W1 내적
    z1 = sigmoid(a1)           # x와 W1 내적 결과 sigmoid 함수 적용 [신경망-1층]
    a2 = np.dot(z1, W2) + b2   # 신경망-1층 결과와 W2 내적
    z2 = sigmoid(a2)           # 신경망-1층 결과와 W2 내적 결과 sigmoid 함수 적용 [신경망-2층]
    a3 = np.dot(z2, W3) + b3   # 신경망-2층 결과와 W3 내적
    y = identify_function(a3)  # 신경망-2층 결과와 W3 내적 결과 항등함수를 통해 출력 [신경망-3층]
    return y

# main
network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y)
