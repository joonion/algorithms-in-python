def Euclid1(n, m):
    if m == 0:
        return n
    else:
        return Euclid1(m, n % m) 

n, m = map(int, input().split())
gcd = Euclid1(n, m) 
print(gcd)
