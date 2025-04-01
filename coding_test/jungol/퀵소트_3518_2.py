def qsort(arr, low, high):
    if low >= high:
        return

    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    arr[i], arr[high] = arr[high], arr[i]

    print(*arr)
    
    qsort(arr, low, i - 1)
    qsort(arr, i + 1, high)
    

n = int(input())
n_arr = list(map(int, input().split()))
qsort(n_arr, 0, n - 1)