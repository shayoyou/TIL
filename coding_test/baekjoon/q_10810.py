n, m = map(int, input().split())
answer = [0] * n
for _ in range(m):
    i, j, k = map(int, input().split())
    for x in range(i-1, j):
        answer[x] = k

print(' '.join(map(str, answer)))