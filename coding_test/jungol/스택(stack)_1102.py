# https://jungol.co.kr/problem/1102?cursor=eyJwcm9ibGVtc2V0Ijo2LCJmaWVsZCI6NiwiaWR4Ijo0fQ==

n = int(input())
stack = []
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'i':
        stack.append(int(cmd[1]))
    elif cmd[0] == 'o':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print("empty")
    else:
        print(len(stack))
