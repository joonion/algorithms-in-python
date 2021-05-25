def find_largest(n, S):
    largest = S[0]
    for i in range(n):
        if largest < S[i]:
            largest = S[i]
    return largest

def find_smallest(n, S):
    smallest = S[0]
    for i in range(n):
        if smallest > S[i]:
            smallest = S[i]
    return smallest

def find_both(n, S):
    largest, smallest = S[0], S[0]
    for i in range(n):
        if largest < S[i]:
            largest = S[i]
        if smallest > S[i]:
            smallest = S[i]
    return largest, smallest

n = int(input())
S = list(map(int, input().split()))
largest, smallest = find_both(n, S)
print(largest, smallest)
