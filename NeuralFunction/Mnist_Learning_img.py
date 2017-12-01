################################################################
#  Neural - 신경망 손글씨 이미지 데이터 인식
#           MNIST Data Set 활용
#           /data/mnist.py 통해 세팅 가능
#           실제 이미지 출력 (숫자 5)
################################################################
import sys
import os

sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

# flatten=True 1차원 Numpy 배열로 저장
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

img = x_train[0]
label = t_train[0]
print(label)  # 5

print(img.shape)          # (784, ) 784개 원소로 이루어진 1차원 배열
img = img.reshape(28, 28) # 원래 이미지 크기인 28 * 28로 변환
print(img.shape)

img_show(img)
