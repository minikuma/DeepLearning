################################################################
#  Perceptron - 인공신경망모델링 Sigmoid 함수
#               임계값을 경계로 출력이 변함 (0 -> 1)
#               선형 분류 (Logical)은 적용하는 범위의 한계가 존재함 (합격/불합격, 스팸메일/정상메일 등)
#               이를 해결하고자 Sigmoid 함수를 도입
################################################################
import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()