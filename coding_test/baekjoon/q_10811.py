# 바구니 뒤집기

n, m = map(int, input().split())
answer = [i for i in range(1, n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    s -= 1
    e -= 1
    while s < e:
        tmp = answer[s]
        answer[s] = answer[e]
        answer[e] = tmp
        s += 1
        e -= 1

print(*answer)