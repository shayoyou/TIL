# https://school.programmers.co.kr/learn/courses/30/lessons/389480

def solution(info, n, m):
    dp = {}

    def solve(idx, a_traces, b_traces):
        if a_traces >= n or b_traces >= m:
            return 1000

        if idx == len(info):
            return a_traces
        
        state = (idx, a_traces, b_traces)
        if state in dp:
            return dp[state]
    
        a_res = solve(idx + 1, a_traces + info[idx][0], b_traces)
        b_res = solve(idx + 1, a_traces, b_traces + info[idx][1])

        dp[state] = min(a_res, b_res)
        return min(a_res, b_res)

    res = solve(0, 0, 0)
    return -1 if res == 1000 else res


print(solution([[1, 2], [2, 3], [2, 1]], 4, 4))
print(solution([[1, 2], [2, 3], [2, 1]], 1, 7))
print(solution([[3, 3], [3, 3]], 7, 1))
print(solution([[3, 3], [3, 3]], 6, 1))