def partition(low, high, S):
    pivot, i, j = S[low], low + 1, high
    while i < j:
        while i <= j and S[i] <= pivot:
            i += 1
        while j >= i and S[j] > pivot:
            j -= 1
        if i < j:
            S[i], S[j] = S[j], S[i]
    S[low], S[j] = S[j], S[low]
    return j # j is the position of the pivot

n = int(input())
S = list(map(int, input().split()))
position = partition(0, n - 1, S)
for i in range(len(S)):
    print(S[i], end=" ")
print()
print(position)
