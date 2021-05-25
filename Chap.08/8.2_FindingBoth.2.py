def find_both(n, S):
    winner, loser = [], []
    for i in range(0, n, 2):
        if i == n - 1:
            winner.append(S[i])
            loser.append(S[i])
        elif S[i] < S[i + 1]:
            winner.append(S[i])
            loser.append(S[i + 1])
        else:
            winner.append(S[i + 1])
            loser.append(S[i])
    return find_largest(winner), find_smallest(loser)

n = int(input())
S = list(map(int, input().split()))
largest, smallest = find_both(n, S)
print(largest, smallest)
