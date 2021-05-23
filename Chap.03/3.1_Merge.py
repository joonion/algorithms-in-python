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

n, m = map(int, input().split())
U = list(map(int, input().split()))
V = list(map(int, input().split()))
S = merge(U, V)
for i in range(len(S)):
    print(S[i], end=" ")
print()