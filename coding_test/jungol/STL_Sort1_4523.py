# https://jungol.co.kr/problem/4523?cursor=eyJwcm9ibGVtc2V0Ijo4LCJmaWVsZCI6MCwiaWR4IjoyfQ==

n = int(input())
arr = list(map(int, input().split()))
s, e = map(int, input().split())

arr[s:e+1] = sorted(arr[s:e+1])
print(*arr)
arr.sort()
print(*arr)