# import numpy as np
# import time

# # 큰 리스트와 NumPy 배열 생성
# list_X = [[i for i in range(1000)] for j in range(1000)]
# np_X = np.array(list_X)

# # 파이썬 리스트 인덱싱 시간 측정
# start = time.time()
# for i in range(1000):
#     for j in range(1000):
#         value = list_X[i][j]
# end = time.time()
# print(f"리스트 인덱싱 시간: {end - start}초")

# # NumPy 배열 인덱싱 시간 측정
# start = time.time()
# for i in range(1000):
#     for j in range(1000):
#         value = np_X[i, j]
# end = time.time()
# print(f"NumPy 인덱싱 시간: {end - start}초")

"""
리스트 인덱싱 시간: 0.11900091171264648초
NumPy 인덱싱 시간: 0.19500255584716797초
"""

############################################################################

import numpy as np
import time

# 큰 리스트와 NumPy 배열 생성
list_X = [[i for i in range(1000)] for j in range(1000)]
np_X = np.array(list_X)

# 리스트에서 모든 값을 2배로 곱하기
start = time.time()
list_result = [[x * 2 for x in row] for row in list_X]
end = time.time()
print(f"리스트 곱셈 시간: {end - start}초")

# NumPy에서 모든 값을 2배로 곱하기 (벡터화 연산)
start = time.time()
np_result = np_X * 2
end = time.time()
print(f"NumPy 곱셈 시간: {end - start}초")

"""
리스트 곱셈 시간: 0.06800007820129395초
NumPy 곱셈 시간: 0.0020034313201904297초
"""