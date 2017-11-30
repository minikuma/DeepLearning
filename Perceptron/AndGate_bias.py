################################################################
#  Perceptron - 인공신경망모델링 AND Gate 구현 -> Bias(편향) 도입
#   - x1, x2 : 입력신호
#   - w1, w2 : 가중치
#   - theta  : 임계값
#   - bias 도입 theta = -b 치환,
#     b + w1*x1 + w2*x2 <  0 --> 0
#     b + w1*x1 + w2*x2 >= 0 --> 1
#     가중치(w)는 입력신호가 결과에 영향도를 조절하는 매개변수, 편향(b)는 얼마나 쉽게 활성화 상태로 변화(1)되느냐를 조절
#     하는 매개 변수  ( 과소적합(Underfiting), 과대적합(Overfiting) ->> 학습과정의 Noise 제거 목적)
################################################################
import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7

    tmp = np.sum(w*x) + b

    if tmp <= 0:
        return 0
    else:
        return 1

print(AND(0, 0)) # 0 값 출력
print(AND(1, 0)) # 0 값 출력
print(AND(0, 1)) # 0 값 출력
print(AND(1, 1)) # 1 값 출력