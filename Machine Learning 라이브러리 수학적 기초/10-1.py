import numpy as np
import torch

X = np.array([[25, 2], [5, 26], [3, 7]]) # 3행 2열의 2차원 배열(행렬)

print(X)

print(X.shape)

print(X.size) # 전체 원소 개수

# 첫번째(0번째)열 슬라이싱
print(X[:, 0])

# 두번째(1번째)행 슬라이싱
print(X[1, :])

# 0~1번째 행/열만 출력
print(X[0:2, 0:2])

# PyTorch에서의 행렬

X_pt = torch.tensor([[25, 2], [5, 26], [3, 7]])
print(X_pt)

print(X_pt.shape)

print(X_pt[1, :])
