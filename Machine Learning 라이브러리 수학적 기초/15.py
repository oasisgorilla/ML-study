import numpy as np
import torch

X = np.array([[25, 2], [5, 26], [3, 7]])
X_pt = torch.tensor(X)
X_pt2 = torch.tensor([[25, 2], [5, 26], [3, 7]])

# 스칼라는 텐서의 모양을 유지하면서 모든 요소에 더해지거나 곱해진다.
print(X * 2)

print(X + 2)

print(X * 2 + 2)

print(X_pt)
print(X_pt2)

print(X_pt * 2 + 2) # 파이썬의 *, + 연산자가 오버로드된다. 
print(torch.add(torch.mul(X_pt, 2), 2)) # 위 코드랑 같은 코드

A = X + 2

print(A + X)

print(A * X) # 아다마르 곱 연산, 행렬의 각 원소끼리의 곱

A_pt = X_pt + 2

print(A_pt * X_pt) # PyTorch에서의 아다마르 곱 연산

C = np.array([[1, 2, 3]]) # (1, 3)
D = np.array([[4], [5], [6]]) # (3, 1)

print(f"* 결과 : \n{C * D}") # shape가 다르면 broadcasting 해준다.

print(f"@ 결과 : {C @ D}") # 내적과는 또 다르다