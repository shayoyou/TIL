# https://jungol.co.kr/problem/5917?cursor=eyJwcm9ibGVtc2V0Ijo2LCJmaWVsZCI6NiwiaWR4Ijo1fQ==

n, t = map(int, input().split())
ready = list(range(1, n + 1))
ready.reverse()
clean = []
dry = []

for _ in range(t):
    c, d = map(int, input().split())
    if c == 1:
        for _ in range(d):
            clean.append(ready.pop())
    else:
        for _ in range(d):
            dry.append(clean.pop())

while dry:
    print(dry.pop())