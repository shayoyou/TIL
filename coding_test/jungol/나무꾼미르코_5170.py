n, m = map(int, input().split())
h_arr = list(map(int, input().split()))

start = 0
end = max(h_arr)

while start <= end:
    mid = (start + end) // 2
    sum = 0
    for h in h_arr:
        if h > mid:
            sum += h - mid
    
    if sum >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)