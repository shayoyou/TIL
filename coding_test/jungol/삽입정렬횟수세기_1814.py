# https://jungol.co.kr/problem/1814?cursor=eyJwcm9ibGVtc2V0Ijo2LCJmaWVsZCI6NiwiaWR4IjozfQ==

n = int(input())
nums = list(map(int, input().split()))
size = len(nums)
result = 0
for i in range(1, size):
    j = i
    while j > 0 and nums[j - 1] > nums[j]:
        temp = nums[j - 1]
        nums[j - 1] = nums[j]
        nums[j] = temp
        result += 1
        j -= 1
print(result)