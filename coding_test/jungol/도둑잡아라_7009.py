# https://jungol.co.kr/problem/7009?cursor=eyJwcm9ibGVtc2V0Ijo4LCJmaWVsZCI6MCwiaWR4Ijo3fQ==

n, m = map(int, input().split())
a = set(map(int, input().split()))
b = list(map(int, input().split()))
res = []
for v in b:
    if v not in a:
        res.append(v)
if res:
    print(*res)
else:
    print(-1)