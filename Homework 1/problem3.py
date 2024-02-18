import math
import random
import time
import matplotlib.pyplot as plt
from tqdm import tqdm


def merge(A: list[int], p: int, q: int, r: int):
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

def merge_sort(A: list[int], p: int, r: int):
    """
    This function implements a recursive Merge-Sort algorithm.
    
    Parameters:
    A (list[int]): A list of integers
    p (int): Represents the starting index to sort 
    r (int): Represents the ending index to sort
    
    Returns:
    void
    """
    
    # Check if the lower bound is in fact lower than the upper bound
    # If not, we are done
    if p < r:
        # q will represent the mid-point
        q = (p + r) // 2
        
        # Sort from the lower bound to the midpoint
        merge_sort(A, p, q)
        
        # Sort from the midpoint to the upper bound
        merge_sort(A, q + 1, r)
        
        # Join the newly sorted sub-lists
        merge(A, p, q, r)

def insertion_sort(A):
    """
    This function implements an Insertion Sort algorithm.
    
    Parameters:
    A (list[int]): A list of integers
    
    Returns:
    void
    """
    for j in range(1, len(A)):
        # KEY is the value we are currently assessing
        key = A[j]
        
        # i is the index of the value exactly 1 spot before KEY 
        i = j - 1
        
        # I.E. : While we have not reached the beginning of the list
        # AND
        # the value 1 index before the KEY is greater than the KEY
        while i >= 0 and A[i] > key:
            # Copy the value of A[i] to the index to it's immediate right
            A[i + 1] = A[i]
            
            # Move to the left
            i -= 1
            
        # Copy the KEY value to the index 1 spot to the right
        # of the last index we compared to
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

        

    

