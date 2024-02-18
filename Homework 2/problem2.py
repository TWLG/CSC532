import random
import matplotlib.pyplot as plt
import time
from heap_sort import heap_sort
from merge_sort import merge_sort

def main():
    sizes = range(100, 10000, 500)
    merge_sort_times = []
    heap_sort_times = []
    for size in sizes:
        A = [random.randint(-1000, 1000) for i in range(size)]
        start = time.perf_counter()
        merge_sort(A, 0, len(A) - 1)
        end = time.perf_counter()
        merge_sort_times.append(end - start)
        start = time.perf_counter()
        heap_sort(A)
        end = time.perf_counter()
        heap_sort_times.append(end - start)
    
    # Plot the times
    plt.plot(sizes, merge_sort_times, label='Merge Sort')
    plt.plot(sizes, heap_sort_times, label='Heap Sort')
    plt.xlabel('Size of Array')
    plt.ylabel('Execution Time (s)')
    plt.title('Execution Time of Merge Sort and Heap Sort Algorithms')
    plt.legend() 
    # Save the plot as heap_vs_merge.png
    # plt.savefig('heap_vs_merge.png')
    plt.show()
    
   

main()