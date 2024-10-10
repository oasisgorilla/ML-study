import numpy as np
import torch

x = np.array([25, 2, 5])
x_pt = torch.tensor(x)

y = np.array([0, 1, 2])
y_pt = torch.tensor(y)

print(np.dot(x, y)) # Numpy 내적
print(x @ y)
print(np.dot(x_pt, y_pt)) # numpy는 텐서도 내적해준다.
print(torch.dot(x_pt, y_pt)) # PyTorch에서의 내적
print(x_pt @ y_pt)

print("--------------------")

x2 = np.array([[25, 2, 5]]) # (1, 3)
x2_pt = torch.tensor(x2)

y2 = np.array([[0, 1, 2]]) # (1, 3)
y2_pt = torch.tensor(y2)

# print(x2 @ y2) # 작동 안함

"""
x2와 y2 모두 (1, 3) shape를 가진 tensor다.
@는 벡터(1차원 tensor)끼리 연산에서는 내적 연산자로 작동하고
다차원 tensor끼리 연산에서는 행렬 곱 연산자로 작동한다.
따라서 아래와 같이 하나를 전치해주면 행렬곱 조건에 맞아서
행렬 곱 연산결과를 보여준다.
"""

print(x2.T @ y2) # (3, 3) 결과
print(x2 @ y2.T) # (1, 1) 결과, 내적과 같은 결과