import numpy as np
import torch

X = np.array([[1, 2], [3, 4]])

print(((1 ** 2) + (2 ** 2) + (3 ** 2) + (4 ** 2)) ** (1/2)) # 각 요소를 제곱하여 더한것의 제곱근이 frobenius norm이다.

print(np.linalg.norm(X)) # L2 norm구할 때 사용했던 함수를 사용하여 구할 수 있다.