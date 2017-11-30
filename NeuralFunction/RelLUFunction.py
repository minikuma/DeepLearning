################################################################
#  Perceptron - 인공신경망모델링 RuLU 함수
#               입력 > 0 -> 입력 = 출력
#               입력 < 0 -> 0 출력
################################################################
import numpy as np
import matplotlib.pylab as plt


def relu(s):
    return np.maximum(0, s)  # 둘 중에 큰 값을 반환


x = np.arange(-6.0, 6.0, 0.1)
y = relu(x)
plt.plot(x, y)
plt.ylim(-1, 5)
plt.show()
