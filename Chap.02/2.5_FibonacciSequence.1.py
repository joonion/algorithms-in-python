def fibo1(n):
    if n <= 1:
        return n
    else:
        return fibo1(n - 1) + fibo1(n - 2)

n = 15
for i in range(n + 1):
    print(fibo1(i), end = " ")
print()
