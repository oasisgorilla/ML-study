import numpy as np
import torch

x = np.array([25, 2, 5], dtype=np.float16)

print(x)

print(len(x))

print(x.shape) # 1차원 배열, 벡터이기 때문에 (3,)으로 표시

x_2 = np.array([[25, 2, 5]])

print(x_2.shape) # x와 똑같은 내용이지만 모양만 다르다.

x_reshaped = x.reshape(1, 3)

print(x_reshaped.shape) # 잘 바뀌었다.

print(x_2.reshape(1, 1, 3)) # 비어있는 차원을 계속 추가할 수 있다.

print(type(x))

print(x[1]) # 두번째 원소

print(type(x[0]))

x_t = x.T # 벡터 전치

print(x_t) # 1차원이기 때문에 전치가 안됨

x_2_t = x_2.T # 2차원으로 만들어준 텐서는 전치가 됨

print(x_2_t)

print(x_2_t.shape)
print(x_2_t.T.shape) # 전치한 행렬을 다시 전치하면 원래대로 돌아옴

z = np.zeros(3)

print(z) # zero 벡터, 어디다 쓰는지 아직은 모르겠다.

x_pt = torch.tensor([25, 2, 5])

print(x_pt) # PyTorch에서의 2차원 tensor 생성

