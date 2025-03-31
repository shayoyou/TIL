# https://www.acmicpc.net/problem/10828

from sys import stdin, stdout
input = stdin.readline
write = stdout.write

mystack = []
size = 0
output = []

n = int(input())
for _ in range(n):
    cmd = input().split()
    command = cmd[0]
    if command == "push":
        mystack.append(int(cmd[1]))
        size += 1
    elif command == "pop":
        if size == 0:
            output.append("-1\n")
        else:
            output.append(f"{mystack.pop()}\n")
            size -= 1
    elif cmd[0] == "size":
        output.append(f"{size}\n")
    elif cmd[0] == "empty":
        output.append("1\n" if size == 0 else "0\n")
    elif cmd[0] == "top":
        output.append("-1\n" if size == 0 else f"{mystack[-1]}\n")

write("".join(output))

