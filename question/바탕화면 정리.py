#  내 풀이
def solution(wallpaper):
    candidate = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                candidate.append((i, j))
    #candidate = [(0, 1), (1, 2), (3, 4)]
    l1 = sorted(candidate, key = lambda x: x[0]) # 튜플 앞 원소 기준으로 정렬
    l2 = sorted(candidate, key = lambda x: x[1]) # 튜플 뒤 원소 기준으로 정렬

    answer = [l1[0][0], l2[0][1], l1[len(l1)-1][0]+1, l2[len(l2)-1][1]+1]
    return answer

# 다른 풇이
def solution(wallpaper):
    x, y = [], [] 
    for i, row in enumerate(wallpaper): #enumerate() : 반복문에서 인덱스와 값을 동시에 꺼낼 때!
        for j, col in enumerate(row):
            if col == '#':
                x.append(i)
                y.append(j)
    return [min(x), min(y), max(x)+1, max(y)+1]