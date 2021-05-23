def bin_search(n, S, x):
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if x == S[mid]:
            return mid
        elif x < S[mid]:
            high = mid - 1
        else: # x > S[mid]
            low = mid + 1
    return -1

n = int(input())
S = list(map(int, input().split()))
T = int(input())
for _ in range(T):
    x = int(input())
    location = bin_search(n, S, x)
    print(location)
