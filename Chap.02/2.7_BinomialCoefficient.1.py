def bino1(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return bino1(n - 1, k - 1) + bino1(n - 1, k)
    
n = 10
for i in range(n + 1):
    for j in range(i + 1):
        print(bino1(i, j), end=" ")
    print()
    