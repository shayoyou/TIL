# https://jungol.co.kr/problem/1697?cursor=eyJwcm9ibGVtc2V0Ijo2LCJmaWVsZCI6NiwiaWR4Ijo3fQ==

n = int(input())
queue = []
front = 0
rear = 0
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'i':
        queue.append(int(cmd[1]))
        rear += 1
    elif cmd[0] == 'o':
        if front == rear:
            print('empty')
        else:
            print(queue[front])
            front += 1
            if front == rear:
                queue.clear()
                front = 0
                rear = 0
    else:
        print(rear - front)
            