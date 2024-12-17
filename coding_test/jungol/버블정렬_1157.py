# https://jungol.co.kr/problem/1157?cursor=eyJwcm9ibGVtc2V0Ijo2LCJmaWVsZCI6NiwiaWR4IjoyfQ==

n = int(input())
nums = list(map(int, input().split()))
size = len(nums)
for i in range(size - 1):
    for j in range(1, size - i):
        if nums[j - 1] > nums[j]:
            temp = nums[j]
            nums[j] = nums[j - 1]
            nums[j - 1] = temp
    print(*nums)