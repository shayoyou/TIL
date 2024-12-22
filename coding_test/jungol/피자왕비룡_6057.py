# https://jungol.co.kr/problem/6057?cursor=eyJwcm9ibGVtc2V0Ijo2LCJmaWVsZCI6NiwiaWR4Ijo5fQ==

from collections import deque

p, n = map(int, input().split())
data = [deque() for _ in range(0, p + 1)]

total = 0
for _ in range(n):
    cmd = list(map(int, input().split()))
    if cmd[0] == 0:
        data[cmd[1]].append(cmd[2])
    else:
        try:
            price = data[cmd[1]].popleft()
            total += price
        except:
            pass
print(total)