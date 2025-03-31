# https://www.acmicpc.net/problem/10870

def solution(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a = 0
    b = 1
    for _ in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return b

print(solution(int(input())))