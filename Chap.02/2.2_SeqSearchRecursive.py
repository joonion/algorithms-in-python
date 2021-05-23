def seq_search2(i, S, x):
    if i == len(S):
        return -1
    elif x == S[i]:
        return i
    else:
        return seq_search2(i + 1, S, x)

n = int(input())
S = list(map(int, input().split()))
T = int(input())
for _ in range(T):
    x = int(input())
    location = seq_search2(0, S, x)
    print(location)
