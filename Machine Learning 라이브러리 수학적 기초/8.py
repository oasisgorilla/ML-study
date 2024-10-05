import numpy as np

x = np.array([25, 2, 5])

print(x)

print((25**2 + 2**2 + 5**2)**(1/2)) # 각 원소를 제곱하여 더한 것의 제곱근

print(np.linalg.norm(x)) # L2 norm

print(np.abs(25) + np.abs(2) + np.abs(5)) # L1 norm

print((25**2 + 2**2 + 5**2)) # 각 원소를 제곱하여 더한 것

print(np.dot(x, x)) # 추후 알아볼 함수라고 한다.

print(np.max([np.abs(25), np.abs(2), np.abs(5)])) # max norm



