import random
import time
from tqdm import tqdm
from heap_sort import heap_sort
from merge_sort import merge_sort
from quick_sort_rpivot import quicksort_rpivot
import matplotlib.pyplot as plt


def main():
    sizes = range(100, 10000, 500)

    merge_sort_times = []
    heap_sort_times = []
    quick_sort_rpivot_times = [] 

    for size in tqdm(sizes):
        A = [random.randint(-1000, 1000) for i in range(size)]
        #A = [i for i in range(size)]

        
        merge_sort_time = 0
        heap_sort_time = 0
        quick_sort_rpivot_time = 0

        for _ in range(5):  # run each algorithm 5 times
            B = list(A)  # copy array
            
            start = time.perf_counter()
            merge_sort(B, 0, len(B) - 1)
            end = time.perf_counter()
            merge_sort_time += end - start

            B = list(A)  
            start = time.perf_counter()
            heap_sort(B)
            end = time.perf_counter()
            heap_sort_time += end - start

            B = list(A)  
            start = time.perf_counter()
            quicksort_rpivot(B, 0, len(B) - 1)
            end = time.perf_counter()
            quick_sort_rpivot_time += end - start

        # average time
        merge_sort_times.append(merge_sort_time / 5)
        heap_sort_times.append(heap_sort_time / 5)
        quick_sort_rpivot_times.append(quick_sort_rpivot_time / 5)

    
    plt.plot(sizes, merge_sort_times, label='Merge Sort')
    plt.plot(sizes, heap_sort_times, label='Heap Sort')
    plt.plot(sizes, quick_sort_rpivot_times, label='Quick Sort Rightmost Pivot')
    plt.xlabel('Size of Array')
    plt.ylabel('Execution Time (s)')
    plt.title('Execution Time of Merge Sort, Heap Sort, and Quick Sort Rightmost Pivot')
    plt.legend() 

    # Save the plot in "Homework 2"
    plt.savefig('Homework 2/Quicksort_RPivot_Comparison_SortedLists.png')
    
    plt.show()


    
   

main()