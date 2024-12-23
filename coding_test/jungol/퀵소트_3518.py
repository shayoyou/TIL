def quicksort(arr, low, high):
    if low >= high:
        return
    pi = partition(arr, low, high)
    print(*arr)
    quicksort(arr, low, pi - 1)
    quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    i = low
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

n = int(input())
arr = list(map(int, input().split()))
quicksort(arr, 0, len(arr) - 1)
