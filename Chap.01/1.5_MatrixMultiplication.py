def print_matrix(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(M[i][j], end=" ")
        print()

def matrix_mult(A, B):
    l, m, n = len(A), len(A[0]), len(B[0])
    C = [[0 for _ in range(n)] for _ in range(l)]
    for k in range(m):
        for i in range(l):
            for j in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C 

l, m, n = map(int, input().split())
A = [[] for _ in range(l)]
for i in range(l):
    A[i] = list(map(int, input().split()))
B = [[] for _ in range(m)]
for i in range(m):
    B[i] = list(map(int, input().split()))
C = matrix_mult(A, B)
print_matrix(C)