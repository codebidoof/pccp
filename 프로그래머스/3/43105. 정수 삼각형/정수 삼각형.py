def solution(triangle):
    n = len(triangle)
    dp = triangle 
    
    for i in range(1, n):
        for j in range(len(triangle[i])):
            
            # 왼쪽 위에서 내려오는 경우                        
            if j == 0:               
                upper_left_value = 0
            else:
                upper_left_value = dp[i-1][j-1]
            
            # 오른쪽 대각선 위에서 내려오는 경우
            if j == i:
                upper_right_value = 0
            else:
                upper_right_value = dp[i-1][j]
                       
            # 두 경로 중 더 큰 누적합을 선택해서 현재 값에 더함                        
            dp[i][j] = dp[i][j] + max(upper_left_value, upper_right_value)                       
    return max(dp[-1])