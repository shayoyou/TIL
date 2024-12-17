# https://jungol.co.kr/problem/1221?cursor=eyJwcm9ibGVtc2V0Ijo2LCJmaWVsZCI6NiwiaWR4Ijo2fQ==

m = int(input())
cmd_list = input().split()
op = ["*", "/", "+", "-"]
nums = []

for cmd in cmd_list:
    if cmd in op:
        if cmd == "/":
            cmd = "//"
        n2 = nums.pop()
        n1 = nums.pop()
        nums.append(eval(f"{n1}{cmd}{n2}"))
    else:
        nums.append(int(cmd))

print(nums[0])