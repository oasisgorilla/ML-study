import numpy as np
import torch

"""
단위행렬은 직교행렬의 예시 중 하나이다.
단위행렬이 직교행렬이라는 것을 증명하는 과정이다.

- 단위행렬의 어떤 두 열/행끼리도 서로 직교한다.
- 각 열은 단위노름을 가진다.

위 두가지를 증명하여 단위행렬은 직교행렬이라는 것을 증명할 수 있다.
"""

I = np.array([[1, 0, 0],[0, 1, 0], [0, 0, 1]])

column_1 = I[:,0] # 1열
column_2 = I[:,1] # 2열
column_3 = I[:,2] # 3열

# 각 열끼리의 내적 구하기
print(np.dot(column_1, column_2)) # 0
print(np.dot(column_1, column_3)) # 0
print(np.dot(column_2, column_3)) # 0

"""
단위행렬의 어떤 두 열도 서로 직교하는 것을 확인하였다.
단위행렬의 전치는 그 자신이다.
모든 열이 직교하면 곧 모든 행도 직교하는 것이므로
열과 행이 모두 직교하여 직교행렬이라는 것이 증명된다.
"""

print(np.linalg.norm(column_1)) # 1.0
print(np.linalg.norm(column_2)) # 1.0
print(np.linalg.norm(column_3)) # 1.0

"""
각 열이 단위노름을 갖고 있는 것을 확인하였고,
이는 각 벡터가 정규직교벡터라는 것을 의미한다.
따라서 Q^(T) Q = I 를 만족하게 된다.
"""

"""
단위행렬이 아닌 행렬K가 직교행렬이라는 것을 증명하는 예시
"""

K = torch.tensor([[2/3, 1/3, 2/3], [-2/3, 2/3, 1/3], [1/3, 2/3, -2/3]])

Kcol_1 = K[:,0] # 1열
print(Kcol_1)
Kcol_2 = K[:,1] # 2열
print(Kcol_2)
Kcol_3 = K[:,2] # 3열
print(Kcol_3)

print(torch.dot(Kcol_1, Kcol_2)) # -3.3114e-09
print(torch.dot(Kcol_1, Kcol_3)) # 3.3114e-09
print(torch.dot(Kcol_2, Kcol_3)) # 6.6227e-09

"""
각 열을 내적한 결과
부동소수점 연산시 오차로 인해서 0에 아주 가까운 수가 나옴
"""

print(torch.norm(Kcol_1)) # 1.0
print(torch.norm(Kcol_2)) # 1.0
print(torch.norm(Kcol_3)) # 1.0

"""
각 열의 노름은 단위노름인 것을 확인함

열이 직교할 뿐만 아니라 모든 열이 단위노름을 갖고 있는 것을 확인했다.

그러나 K^(T) =! K 이므로 
K의 모든 행이 직교한다는 것을 증명해봐야 한다.

혹은 K^(T)K = I 식을 만족하는지 확인하여 직교행렬인지 확인할 수도 있다.
"""

Krow_1 = K[0,:] # 1행
Krow_2 = K[1,:] # 2행
Krow_3 = K[2,:] # 3행

print(torch.dot(Krow_1, Krow_2)) # 0.
print(torch.dot(Krow_1, Krow_3)) # 0.
print(torch.dot(Krow_2, Krow_3)) # 0.

"""
위 결과에서 K의 그 어떤 행들도 서로 직교하는 것을 확인했다.
따라서 K는 직교행렬인 것을 확인했다.
"""

print(torch.matmul(K.T,K)) # tensor([[ 1.0000e+00, -3.3114e-09,  3.3114e-09], [-3.3114e-09,  1.0000e+00,  6.6227e-09], [ 3.3114e-09,  6.6227e-09,  1.0000e+00]])

"""
위 결과에서 끝수처리 오차가 있지만, 단위행렬(I)이 도출되었으므로
K는 K^(T)K = I 를 만족하여 직교행렬이다.
"""