################################################################
#  Perceptron - 인공신경망모델링 XOR 구현
#     Perceptron의 한계
#     AND, OR, NAND Gate인 경우 출력값을 선형적(직선)으로 구분할수 있지만,
#     XOR Gate인 경우 선형적(직선)으로 구분이 되지 않는다.
#     해결방안 -> 다중 퍼셉트론 구조로 변경
#                 XOR Gate = [NAND 출력] [AND연산] [OR 출력]로 구현
#     XOR Gate 특징: 같으면 0, 다르면 1의 값을 출력
################################################################
import numpy as np

def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2

    if tmp <= theta:
        return 0

    elif tmp > theta:
        return 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7

    tmp = np.sum(w*x) + b      # w1*x1 + w2*x2 + b

    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2

    tmp = np.sum(w * x) + b    # w1*x1 + w2*x2 + b

    if tmp <= 0:
        return 0
    else:
        return 1

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y  = AND(s1, s2) # NAND의 출력과 OR의 출력의 AND 연산
    return y

print(XOR(0,0))  # 0을 출력
print(XOR(1,0))  # 1을 출력
print(XOR(0,1))  # 1을 출력
print(XOR(1,1))  # 0을 출력