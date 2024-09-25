import numpy as np
import matplotlib.pyplot as plt

# 시간과 거리 데이터 설정
time = np.linspace(0, 40, 1000)  # 0에서 40분까지 1000개의 시간 좌표 생성

# 강도와 보안관의 이동 거리 계산
distance_robber = 2.5 * time  # 강도가 이동한 거리 (속도: 2.5 km/min)
distance_sheriff = 3 * (time - 5)  # 보안관이 5분 늦게 출발 (속도: 3 km/min)

# 그래프 그리기
fig, ax = plt.subplots()
plt.title('A Bank Robber Caught')  # 제목 설정
plt.xlabel('time(in min)')  # x축 레이블
plt.ylabel('distance(in km)')  # y축 레이블
ax.set_xlim([0, 40])  # x축 범위 설정
ax.set_ylim([0, 100])  # y축 범위 설정
ax.plot(time, distance_robber, c='green', label='Robber')  # 강도 거리 그래프
ax.plot(time, distance_sheriff, c='brown', label='Sheriff')  # 보안관 거리 그래프

# 30분에서 수직선, 75km에서 수평선 추가
plt.axvline(x=30, color='purple', linestyle='--')  # 수직선
plt.axhline(y=75, color='purple', linestyle='--')  # 수평선

plt.legend()  # 범례 추가
plt.show()  # 그래프 표시