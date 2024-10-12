import numpy as np
import torch


X_sym = np.array([[0, 1, 2], [1, 7, 8], [2, 8, 9]]) # 대칭행렬

print(X_sym)

print(X_sym.T)

print(X_sym == X_sym.T) # 이렇게 각 요소가 같은지 확인 가능

I = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) # 단위행렬
print(I)

x_pt = torch.tensor([25, 2, 5])
print(x_pt)

print(torch.matmul(I, x_pt)) # 단위행렬에 적절한 행렬이나 벡터를 곱하면 해당 행렬이나 벡터가 그대로 나온다.(항등원)
