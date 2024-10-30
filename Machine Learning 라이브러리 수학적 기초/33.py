import numpy as np
import matplotlib.pyplot as plt

v = np.array([3, 1])

def plot_vectors(vectors, colors):
    """
    Plot one or more vectors in a 2D plane, specifying a color for each. 

    Arguments
    ---------
    vectors: list of lists or of arrays
        Coordinates of the vectors to plot. For example, [[1, 3], [2, 2]] 
        contains two vectors to plot, [1, 3] and [2, 2].
    colors: list
        Colors of the vectors. For instance: ['red', 'blue'] will display the
        first vector in red and the second in blue.
        
    Example
    -------
    plot_vectors([[1, 3], [2, 2]], ['red', 'blue'])
    plt.xlim(-1, 4)
    plt.ylim(-1, 4)
    """
    plt.figure()
    plt.axvline(x=0, color='lightgray')
    plt.axhline(y=0, color='lightgray')

    for i in range(len(vectors)):
        x = np.concatenate([[0,0],vectors[i]])
        plt.quiver([x[0]], [x[1]], [x[2]], [x[3]],
                   angles='xy', scale_units='xy', scale=1, color=colors[i],)
        
"""
np.concatenate는 Numpy에서 배열을 연결하여 하나의 배열로 만들어주는 메서드이다.
여러 배열을 결합할 때 사용하고, axis= 특성을 사용하여 연결 축을 지정할 수 있다.

a = [[1, 2],
     [3, 4]]

b = [[5, 6],
     [7, 8]]

위의 배열 a, b를 연결하는 경우
np.concatenate((a, b), axis=0)
np.concatenate((a, b), axis=1)
두 가지로 연결할 수 있다.

axis=0으로 연결할 때
[[1, 2],
 [3, 4],
 [5, 6],
 [7, 8]]

 행을 기준으로 아래로 연결되며(행이 늘어남), 두 배열이 세로로 쌓임

axis=1로 연결할 때
[[1, 2, 5, 6],
 [3, 4, 7, 8]]

 열을 기준으로 옆으로 연결되며(열이 늘어남), 두 배열이 가로로 이어짐
"""

plot_vectors([v], ['lightblue'])
plt.xlim(-1, 5) # x좌표값의 범위를 지정
_ = plt.ylim(-1, 5) # y좌표값의 범위를 지정
# plt.show() # 플롯을 화면에 출력

I = np.array([[1, 0], [0, 1]]) # 단위 벡터

Iv = np.dot(I, v) # array([3, 1])

v == Iv # array([True, True])

E = np.array([[1, 0], [0, -1]]) # x축을 기준으로 뒤집기 위한 행렬 E
Ev = np.dot(E, v) # array([3, -1])

plot_vectors([v, Ev], ['lightblue', 'blue'])
plt.xlim(-1, 5)
_ = plt.ylim(-3, 3)
# plt.show()

F = np.array([[-1, 0], [0, 1]]) # y축을 기준으로 뒤집기 위한 행렬 F
Fv = np.dot(F, v)

plot_vectors([v, Fv], ['lightblue', 'blue'])
plt.xlim(-4, 4)
_ = plt.ylim(-1, 5)
# plt.show()

"""
행렬 A에 벡터 v를 곱해보고, 다른 벡터 v2도 곱해봄
"""

A = np.array([[-1, 4], [2, -2]]) # 예시 행렬 A
Av = np.dot(A, v)

plot_vectors([v, Av], ['lightblue', 'blue'])
plt.xlim(-1, 5)
_ = plt.ylim(-1, 5)
# plt.show()

v2 = np.array([2, 1])
plot_vectors([v2, np.dot(A, v2)], ['lightgreen', 'green'])
plt.xlim(-1, 5)
_ = plt.ylim(-1, 5)
# plt.show()

"""
여러 벡터에 행렬을 한 번에 곱하기 위해서는 벡터를 합쳐야 한다.
먼저 벡터를 2차원 행렬로 바꿔주고, 전치하여 열벡터로 만들어준다.
이 벡터들을 np.concatenate를 사용해서 axis=1(열 기준)로 합쳐준다.
"""
v3 = np.array([-3, -1]) # v의 반사 벡터
v4 = np.array([-1, 1])

V = np.concatenate((np.matrix(v).T,
                   np.matrix(v2).T,
                   np.matrix(v3).T,
                   np.matrix(v4).T),
                   axis=1)

"""
V = [[ 3  2 -3 -1]
     [ 1  1 -1  1]]

4개의 열벡터를 합친 행렬을 얻음
"""

AV = np.dot(A, V)

"""
행렬의 열을 다시 1차원 벡터로 변환해주는 함수를 사용하여
AV의 각 열벡터를 출력해봄
벡터의 위치에 따라 아핀 변형의 결과가 다양하게 달라질 수 있음
"""

# 행렬의 열을 다시 1차원 벡터로 변환해주는 함수
def vectorfy(mtrx, clmn):
    return np.array(mtrx[:, clmn]).reshape(-1)

plot_vectors([vectorfy(V, 0), vectorfy(V, 1), vectorfy(V, 2), vectorfy(V, 3),
             vectorfy(AV, 0), vectorfy(AV, 1), vectorfy(AV, 2), vectorfy(AV, 3)], 
            ['lightblue', 'lightgreen', 'lightgray', 'orange',
             'blue', 'green', 'gray', 'red'])

plt.xlim(-4, 6)
_ = plt.ylim(-5, 5)
# plt.show()



