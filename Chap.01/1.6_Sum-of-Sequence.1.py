def sum_of_seq(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

n = int(input())
s = sum_of_seq(n)
print(s)
