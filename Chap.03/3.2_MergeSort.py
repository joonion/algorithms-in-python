def merge(U, V):
    n, m = len(U) + len(V), min(len(U), len(V))
    S, i, j, k = [0] * n, 0, 0, 0
    while i < m and j < m:
        if U[i] <= V[j]:
            S[k] = U[i]
            i += 1
        else: # U[i] > V[j]
            S[k] = V[j]
            j += 1
        k += 1
    while i < len(U):
        S[k] = U[i]
        i, k = i + 1, k + 1
    while j < len(V):
        S[k] = V[j]
        j, k = j + 1, k + 1
    return S

def mergesort(S):
    print(S)
    if len(S) <= 1:
        return S
    else:
        mid = len(S) // 2
        U = mergesort(S[:mid])
        V = mergesort(S[mid:len(S)])
        return merge(U, V)

n = int(input())
S = list(map(int, input().split()))
V = mergesort(S)
for i in range(len(V)):
    print(V[i], end=" ")
print()