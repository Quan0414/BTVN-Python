def binary_search(arr, x):
    arr.sort()
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = r + 1
        else:
            r = mid - 1
    return -1

n = int(input())
arr = [int(input()) for i in range(n)]
x = int(input())

print(binary_search(arr, x))