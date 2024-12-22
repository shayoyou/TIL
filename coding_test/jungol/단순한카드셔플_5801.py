# https://jungol.co.kr/problem/5801?cursor=eyJwcm9ibGVtc2V0Ijo2LCJmaWVsZCI6NiwiaWR4Ijo4fQ==

n = int(input())
data = list(range(1, n + 1))
front = 0
rear = 0
size = n
flag = True
while size:
    num = data[front]
    front = (front + 1) % n
    if flag:
        print(num, end=' ')
        size -= 1
    else:
        data[rear] = num
        rear = (rear + 1) % n
    flag = not flag