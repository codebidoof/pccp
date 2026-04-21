def solution(dirs):
    mySet = set() # 경로를 저장할 셋
    x, y = (0, 0) # 현재 좌표
    direction = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)} # dx, dy
    
    for d in dirs:
        dx, dy = direction[d]
        nx = x + dx
        ny = y + dy
        
        if -5 <= nx <= 5 and -5 <= ny <= 5: # 범위 이내라면 
            mySet.add((x, y, nx, ny))
            mySet.add((nx, ny, x, y))
            
            # 현재위치 갱신
            x = nx
            y = ny
    return len(mySet) // 2