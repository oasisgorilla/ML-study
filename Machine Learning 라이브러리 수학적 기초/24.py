import numpy as np
import torch

A = np.array([[3, 4],
             [5, 6],
             [7, 8]])

B = np.array([[1, 9],
             [2, 0]])

print(np.dot(A, B)) # np.dot()함수는 1차원 텐서끼리는 내적을, 2차원 텐서끼리는 행렬곱을, 다차원 텐서끼리는 다차원 곱연산을 한다.

# np.dot(B, A) # 이 연산은 작동하지 않는다. A열과 B행을 맞춰주는 행렬곱의 조건을 만족하지 않기 때문이다.

A_pt = torch.tensor(A)

# 다음은 모두 같은 결과를 얻는 tensor 정의법이다.
B_pt = torch.from_numpy(B)
print(B_pt)

B_pt = torch.tensor([[1, 2], [9, 0]]).T
print(B_pt)

B_pt = torch.tensor(B)
print(B_pt)

print(torch.matmul(A_pt, B_pt))
# print(torch.dot(A_pt, B_pt))

"""
np.dot()은 알아서 텐서의 차원을 구분하여 내적과 행렬곱을 적절히 수행하지만
torch.dot()은 torch.matmul()과 구분해서 사용해줘야 한다.
"""