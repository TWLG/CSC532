from merge_sort import merge_sort
from heap_sort import heap_sort
from random_pivot_quicksort import randomized_quicksort
import time
import random
from tqdm import tqdm
import matplotlib.pyplot as plt

def main():
    sizes = range(100, 10000, 500)

    heap_sort_times = []
    merge_sort_times = []
    quicksort_random_pivot_times = []

    for size in tqdm(sizes):
        #A = [random.randint(-1000, 1000) for i in range(size)]
        A = [i for i in range(size)]

        
        merge_sort_time = 0
        heap_sort_time = 0
        quick_sort_random_pivot_time = 0

        for _ in range(5):  # run each algorithm 5 times
            # Generate already sorted array
            
            B = list(A)
            start = time.perf_counter()
            heap_sort(B)
            end = time.perf_counter()
            heap_sort_time += end - start

            # Test Merge Sort
            B = list(A)
            start = time.perf_counter()
            merge_sort(B, 0, len(B) - 1)
            end = time.perf_counter()
            merge_sort_time += end - start

            # Test Quicksort with randomly selected pivot
            B = list(A)
            start = time.perf_counter()
            randomized_quicksort(B, 0, len(B) - 1)
            end = time.perf_counter()
            quick_sort_random_pivot_time += end - start
        
        
        # average time
        merge_sort_times.append(merge_sort_time / 5)
        heap_sort_times.append(heap_sort_time / 5)
        quicksort_random_pivot_times.append(quick_sort_random_pivot_time / 5)
        
    
    plt.plot(sizes, heap_sort_times, label='Heap Sort')
    plt.plot(sizes, merge_sort_times, label='Merge Sort')
    plt.plot(sizes, quicksort_random_pivot_times, label='Quicksort Random Pivot')
    plt.xlabel('Size of Array')
    plt.ylabel('Execution Time (s)')
    plt.title('Execution Time of Sorting Algorithms on Already Sorted Arrays')
    plt.legend()
    plt.grid(True)

    # Save the plot in "Homework 2"
    #plt.savefig('Homework 2/Random Pivot_SortedLists.png')
    
    plt.show()

main()
