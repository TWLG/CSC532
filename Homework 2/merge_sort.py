import math

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = (n1 + 1) * [0]
    R = (n2 + 1) * [0]

    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + j + 1]
    L[-1] = math.inf
    R[-1] = math.inf

    i = j = 0

    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)