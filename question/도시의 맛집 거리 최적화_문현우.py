#주어진 두 정수와 도시 정보를 입력받음
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

homes = []
restaurants = []

# 브루트 포스 방식으로 arr의 모든 원소를 탐색
for i in range(N): # 행
    for j in range(N): # 열
        if arr[i][j] == 1:
            homes.append([i, j])
        elif arr[i][j] == 2:
            restaurants.append([i, j])

from itertools import combinations
mi = 1000

for comb_r in combinations(restaurants, M): # 맛집 M개 선택
    temp = 0 # 최소 거리 합을 저장하는 임시 변수
    for h in homes:
        dist = min([abs(h[0]-rx) + abs(h[1]-ry) for (rx, ry) in comb_r]) # 각 집마다 최소 거리 계산
        temp += dist
    result = min(mi, temp)

print(result)