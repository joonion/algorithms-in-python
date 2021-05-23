def bino2(n, k):
    B = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                B[i][j] = 1
            else:
                B[i][j] = B[i - 1][j - 1] + B[i - 1][j]
    
n = 10
for i in range(n + 1):
    for j in range(i + 1):
        print(bino2(i, j), end=" ")
    print()