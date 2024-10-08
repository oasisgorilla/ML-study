import numpy as np
import torch

X = np.array([[25, 2], [5, 26], [3, 7]])
X_pt = torch.tensor(X)

print(X.sum())

print(torch.sum(X_pt))

"""
위 과정으로 2차원 텐서가 스칼라 값이 되었다. 
이렇게 차원이 줄어드는 것을 리덕션이라고 한다.
"""

print(X.sum(axis=0))
print(torch.sum(X_pt, 0))

X_sum = X.sum(axis=0)

print(X_sum.shape)
"""
axis=n은 해당 축(차원)을 따라 합하라는 뜻이다.
2차원 텐서에서는 0과 1까지, 3차원 텐서에서는 0, 1, 2까지 있다.
위의 2차원 텐서 X는 3행 2열의 텐서로 (3, 2)의 shape를 갖는다.
axis=0은 3, axis=1은 2이다.
X.sum(axis=0)을 하게되면 (3, 2)의 shape가 (2,)의 shape로 변한다.
차원이 줄었으니 reduction이 일어났다.
"""
# 4차원 텐서 생성 (2개의 이미지, 3개의 채널, 4x4 크기)
X_4 = np.random.rand(2, 3, 4, 4)

# axis=0: 배치 차원에 대해 합산
print(X_4.sum(axis=0).shape)  # 결과: (3, 4, 4)

# axis=1: 채널 차원에 대해 합산
print(X_4.sum(axis=1).shape)  # 결과: (2, 4, 4)

# axis=2: 높이 차원에 대해 합산
print(X_4.sum(axis=2).shape)  # 결과: (2, 3, 4)

# axis=3: 너비 차원에 대해 합산
print(X_4.sum(axis=3).shape)  # 결과: (2, 3, 4)

"""
위 처럼 axis= 에 지우고 싶은 차원의 인덱스를 쓰면 지워지는 것으로 이해하고 쓰면 편할 듯 하다.
"""
