# https://www.acmicpc.net/problem/2566

max_ = 0
row, col = 0, 0
for i in range(9):
    nums = list(map(int, input().split()))
    for j in range(9):
        if nums[j] > max_:
            max_ = nums[j]
            row = i
            col = j

print(max_)
print(row + 1, col + 1)