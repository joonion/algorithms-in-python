def seq_search(n, S, x):
    for i in range(n):
        if S[i] == x:
            return i
    return -1

n = int(input())
S = list(map(int, input().split()))
T = int(input())
for _ in range(T):
    x = int(input())
    location = seq_search(n, S, x)
    print(location)
