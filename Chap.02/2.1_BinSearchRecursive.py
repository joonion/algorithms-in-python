def bin_search2(low, high, S, x):
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if x == S[mid]:
            return mid
        elif x < S[mid]:
            return bin_search2(low, mid - 1, S, x)
        else: # x > S[mid]
            return bin_search2(mid + 1, high, S, x)

n = int(input())
S = list(map(int, input().split()))
T = int(input())
for _ in range(T):
    x = int(input())
    location = bin_search2(0, n - 1, S, x)
    print(location)
