def find_largest(n, S):
    largest = S[0]
    for i in range(n):
        if largest < S[i]:
            largest = S[i]
    return largest

n = int(input())
S = list(map(int, input().split()))
s = find_largest(n, S)
print(s)
