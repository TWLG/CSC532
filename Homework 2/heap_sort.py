

def get_parent(i):
    return (i - 1) // 2

def get_left(i):
    return 2 * i + 1

def get_right(i):
    return 2 * i + 2

def max_heapify(A, i):
    size = len(A)
    l = get_left(i)
    r = get_right(i)
    if l < size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)

def build_max_heap(A):
    heap_size = len(A)
    i = heap_size // 2 - 1
    while i >= 0:
        max_heapify(A, i)
        i -= 1

def heap_sort(A):
    build_max_heap(A)
    heap_size = len(A)
    for i in range(heap_size - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        max_heapify(A, 0)
    return A

