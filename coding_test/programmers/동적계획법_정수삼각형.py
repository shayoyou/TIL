def solution(triangle):
    dp = [0] * len(triangle)
    dp[0] = triangle[0][0]
    
    for i in range(1, len(triangle)):
        temp_dp = [0] * len(triangle)
        for j in range(i + 1):
            if j == 0:
                temp_dp[j] = dp[0] + triangle[i][j]
            elif j == i:
                temp_dp[j] = dp[j-1] + triangle[i][j]
            else:
                temp_dp[j] = max(dp[j-1], dp[j]) + triangle[i][j]
        dp = temp_dp
    
    return max(dp)


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))