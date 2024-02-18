import math
import random
import time
import matplotlib.pyplot as plt
from tqdm import tqdm


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

def insertion_sort(A: list):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key

def main(): 
    sizes = range(100, 10000, 500)
    merge_sort_times = []
    insertion_sort_times = []
    for size in tqdm(sizes, desc='Processing'):
        A = [random.randint(-1000, 1000) for i in range(size)]
        start = time.perf_counter()
        merge_sort(A, 0, len(A) - 1)
        end = time.perf_counter()
        merge_sort_times.append(end - start)
        start = time.perf_counter()
        insertion_sort(A)
        end = time.perf_counter()
        insertion_sort_times.append(end - start)

    # Plot the times
    plt.plot(sizes, merge_sort_times, label='Merge Sort')
    plt.plot(sizes, insertion_sort_times, label='Insertion Sort')
    plt.xlabel('Size of Array')
    plt.ylabel('Execution Time (s)')
    plt.title('Execution Time of Merge Sort and Insertion Sort Algorithms')
    plt.legend()
    plt.show()

main()

        

    

