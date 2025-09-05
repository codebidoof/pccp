#1. 내 답
def mx(park):
    dv = [y for y in range(len(park))] #세로, [0, 1, 2, 3, 4, 5]
    dh = [x for x in range(len(park))] #가로
    for i in range(len):
        pass # 모르겠어...

def solution1(mats, park):
    return -1

#2. 타인의 답안 - 이사람 천재임..?ㄷㄷ
def solution(mats, park):
    mats = sorted(mats, reverse = True) # 큰것부터 검사하기 위해 내림차순 정렬 [5, 3, 2]
    M, N = len(park), len(park[0]) # 세로, 가로 크기

    for l in mats:
        startIdxSet = set((i,j) for i in range(M-l+1) for j in range(N-l+1)) # 0 ~ M-1, 0 ~ N-1
        for a, b in startIdxSet:
            ret = set()
            for i in range(a,a+l): # 브루트포스
                for j in range(b,b+l):
                    ret.add(park[i][j])
            if ret == {'-1'}:
                return l
    return -1