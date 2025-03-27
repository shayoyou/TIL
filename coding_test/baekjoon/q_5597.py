# 과제 안 내신 분..?

nums = [0] * 30
for _ in range(28):
    n = int(input())
    nums[n - 1] = 1

for i in range(30):
    if nums[i] == 0:
        print(i + 1, end=' ')