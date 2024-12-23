# https://jungol.co.kr/problem/7009?cursor=eyJwcm9ibGVtc2V0Ijo4LCJmaWVsZCI6MCwiaWR4Ijo3fQ==

# ver.1
# n, m = map(int, input().split())
# a = set(map(int, input().split()))
# b = list(map(int, input().split()))
# res = []
# for v in b:
#     if v not in a:
#         res.append(v)
# if res:
#     print(*res)
# else:
#     print(-1)

# ver.2
def search(arr, v):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == v:
            return True
        elif arr[mid] > v:
            high = mid - 1
        else:
            low = mid + 1
    return False

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
res = []
for b in B:
    if not search(A, b):
        res.append(b)

if res:
    print(*res)
else:
    print(-1)