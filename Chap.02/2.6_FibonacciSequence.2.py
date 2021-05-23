def fibo2(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
    return b

n = 15
for i in range(n + 1):
    print(fibo2(i), end = " ")
print()
