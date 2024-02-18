def partition(A, p, r):
    x = A[r]  # x is the rightmost element for pivot.
    i = p - 1  # i is the index of the smaller element.

    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quicksort_rpivot(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort_rpivot(A, p, q - 1)
        quicksort_rpivot(A, q + 1, r)

