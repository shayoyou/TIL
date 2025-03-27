# 공 바꾸기
n, m = map(int, input().split())
n_arr = [i for i in range(1, n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    tmp = n_arr[i - 1]
    n_arr[i - 1] = n_arr[j - 1]
    n_arr[j - 1] = tmp

print(" ".join(map(str, n_arr)))