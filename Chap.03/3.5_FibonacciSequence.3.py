def fibo3(n, F):
    if n <= 1:
        F[n] = n
    elif F[n] == -1:
        F[n] = fibo3(n - 1, F) + fibo3(n - 2, F)
    return F[n]

n = 15
F = [-1] * (n + 1)
for i in range(n + 1):
    print(fibo3(i, F), end = " ")
print()
