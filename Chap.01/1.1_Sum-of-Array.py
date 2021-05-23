def sum_of_array(n, S):
    s = 0
    for i in range(n):
        s += S[i]
    return s

n = int(input())
S = list(map(int, input().split()))
s = sum_of_array(n, S)
print(s)
