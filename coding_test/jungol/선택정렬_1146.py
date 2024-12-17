# https://jungol.co.kr/problem/1146?cursor=eyJwcm9ibGVtc2V0Ijo2LCJmaWVsZCI6NiwiaWR4IjowfQ==

n = int(input())
nums = list(map(int, input().split()))
size = len(nums)
for i in range(size - 1):
    small_idx = i
    for j in range(i + 1, size):
        if nums[j] < nums[small_idx]:
            small_idx = j
    
    temp = nums[i]
    nums[i] = nums[small_idx]
    nums[small_idx] = temp

    print(*nums)