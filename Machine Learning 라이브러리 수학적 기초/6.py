import torch

# 스칼라는 기본적인 변수와 비슷하게 사용한다.
x = 25
print(x)

print(type(x))

y = 3

py_sum = x + y
print(py_sum)

x_float = 25.0
float_sum = x_float + y 

print(type(float_sum)) # y는 int였지만, float와 연산하면 자동으로 float으로 바뀌어 계산됨

# PyTorch에서의 스칼라 사용
x_pt = torch.tensor(25) # 25의 스칼라 생성

x_pt = torch.tensor(25, dtype=torch.float16) # data type을 정해줄 수도 있음

print(x_pt)

print(x_pt.shape) # 스칼라는 0차원이라 shape가 []로 나온다.

"""
python 3.12버전부터 distutils 모듈이 삭제됨
3.11로 다운그레이드 해줘야한다고 함
pip install --upgrade setuptools를 해서 해결
이후 google모듈이 필요하다는 오류가 나와서
pip install protobuf를 설치함
pip install google도 함
가상환경에도 해봄
안됨
tensorflow는 colab에서만 돌리기로 했다.
tensorflow는 버전을 잘 맞춰줘야해서 colab이나 아나콘다같은 환경에서 돌리는 것을
추천한다.
"""