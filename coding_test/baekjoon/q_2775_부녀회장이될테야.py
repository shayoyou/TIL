# https://www.acmicpc.net/problem/2775

def solution(k, n):
    arr = [i for i in range(1, n+1)]
    for _ in range(0, k):
        sum = 1
        for j in range(1, n):
            sum = sum + arr[j]
            arr[j] = sum
            
    return arr[n-1]

t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    print(solution(k, n))