################################################################
#  Perceptron - 인공신경망모델링 계단함수
#               임계값을 경계로 출력이 변함 (0 -> 1)
################################################################
import numpy as np
import matplotlib.pylab as plt


def step_function(s):
    return np.array(s > 0, dtype=np.int)


x = np.arange(-5.0, 5.0, 0.1)  # -5.0 ~ 5.0 0.1 간격
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
