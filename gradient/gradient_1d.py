################################################################
#  Gradient - 수치 미분 구현
#             2차함수 x = 5에서 접선의 기울기
#             해석적 (실제 미분값) 미분과 수치적 (근사값) 미분의 차이
################################################################
import numpy as np
import matplotlib.pylab as plt

def numerical_diff(f, x):
    h = 1e-4  # 중앙차분 계산 h의 값을 0으로 근접하기 위한 값 세팅
    return (f(x+h) - f(x-h)) / (2*h)

def function_1(x):
    return 0.01*x**2 + 0.1*x   # y = (0.01*x)2 + 0.1*x 2차 함수

def tangent_line(f, x):
    d = numerical_diff(f, x)
    print(d)                # 0.199999999~
    y = f(x) - d*x          # (0.01*5**2 + 0.1*5) - (0.1999999*5) = 0.75 - 0.9999999999~
    print(f(x))             # (0.01*5**2 + 0.1*5) = 0.75
    print(y)                # 0.75 - 0.9999999999~ = -0.249999999~
    return lambda t: d*t + y

x = np.arange(0.0, 20.0, 0.1)  # 0 ~ 20까지 0.1 간격의 배열 생성
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")

tf = tangent_line(function_1, 5)
y2 = tf(x)

plt.plot(x, y)
plt.plot(x, y2)
plt.show()