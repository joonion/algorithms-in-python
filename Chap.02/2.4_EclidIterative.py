def Euclid2(n, m):
    while m != 0:
        n, m = m, n % m
    return n

n, m = map(int, input().split())
gcd = Euclid2(n, m) 
print(gcd)
