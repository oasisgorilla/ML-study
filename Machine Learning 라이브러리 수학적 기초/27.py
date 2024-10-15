import numpy as np
import torch

X = np.array([[4, 2], [-5, -3]])
Xinv = np.linalg.inv(X)
print(Xinv) # X의 역행렬

y = np.array([4, -7])

w = np.dot(Xinv, y) # X역행렬과 y 곱

print(w)

print(np.dot(X, w)) # y = Xw

X_pt = torch.tensor(X, dtype=torch.float32)

"""
역행렬(inverse)을 계산하기 위해서는 소수점 연산이 필요하기 때문에 
정수형 텐서의 데이터 타입을 부동소수점(float)이나 복소수(complex)형으로 바꿔줘야 함
"""

print(torch.inverse(X_pt))

X2 = np.array([[-4, 1], [-8, 2]]) # 특이행렬(교차하지 않는 두 직선)

# X2inv = np.linalg.inv(X2)