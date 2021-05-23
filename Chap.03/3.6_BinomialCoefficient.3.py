def bino3(n, k, B):
    if k == 0 or k == n:
        B[n][k] = 1
    elif B[n][k] == -1:
        B[n][k] = bino3(n - 1, k - 1, B) + bino3(n - 1, k, B)
    return B[n][k]
    
n = 10
B = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(n + 1):
    for j in range(i + 1):
        print(bino3(i, j, B), end=" ")
    print()
    