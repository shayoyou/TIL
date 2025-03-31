# https://www.acmicpc.net/problem/2738

n, m = map(int, input().split())

mat_a = []
for _ in range(n):
    mat_a.append(list(map(int, input().split())))

mat_b = []
for _ in range(n):
    mat_b.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        print(mat_a[i][j] + mat_b[i][j], end=" ")
    print()