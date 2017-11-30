################################################################
#  Perceptron - 인공신경망모델링 NAND/OR Gate 구현
#   - x1, x2 : 입력신호
#   - w1, w2 : 가중치
#   - theta  : 임계값
#   - NAND / OR Gate는 AND Gate와 가중치와 편향 값만 다름
#     기존 Modeling은 그대로이고, 가중치와 편향 값 조정으로 AND/OR/NAND Gate 구현 가능
################################################################
import numpy as np

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

print(NAND(0, 0)) # 1 값 출력
print(NAND(1, 0)) # 1 값 출력
print(NAND(0, 1)) # 1 값 출력
print(NAND(1, 1)) # 0 값 출력

print(OR(0, 0)) # 0 값 출력
print(OR(1, 0)) # 1 값 출력
print(OR(0, 1)) # 1 값 출력
print(OR(1, 1)) # 1 값 출력