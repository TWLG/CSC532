import random
import time
from tqdm import tqdm
from quick_sort_rpivot import quicksort_rpivot
import matplotlib.pyplot as plt
from statistics import median
import sys

sys.setrecursionlimit(10000)

def main():
    # sizes = range(100, 10000, 500)
    sizes = range(100, 5000, 500)

    qs_random_pivot_times = []
    qs_rpivot_times = []
    qs_median_three_times = [] 

    for size in tqdm(sizes):
        # A = [random.randint(-1000, 1000) for i in range(size)]
        A = [i for i in range(size)]
        
        qs_random_pivot_time = 0
        qs_rpivot_time = 0
        qs_median_three_time = 0

        for _ in range(5):  # run each algorithm 5 times
            
            #TODO imprt p4 algo
            # B = list(A)  
            # start = time.perf_counter()
            # quicksort_rpivot(B, 0, len(B) - 1)
            # end = time.perf_counter()
            # qs_random_pivot_time += end - start

            B = list(A)  
            start = time.perf_counter()
            quicksort_rpivot(B, 0, len(B) - 1)
            end = time.perf_counter()
            qs_rpivot_time += end - start

            B = list(A)
            x = [B[0],B[len(B)//2],B[-1]]
            pivot = median(x)
            start = time.perf_counter()
            quicksort_rpivot(B, 0, pivot)
            end = time.perf_counter()
            qs_median_three_time += end - start

        # average time
        qs_random_pivot_times.append(qs_random_pivot_time / 5)
        qs_rpivot_times.append(qs_rpivot_time / 5)
        qs_median_three_times.append(qs_median_three_time / 5)
    
    # plt.plot(sizes, qs_random_pivot_times, label='Merge Sort')
    plt.plot(sizes, qs_rpivot_times, label='Quick Sort Rightmost Pivot')
    plt.plot(sizes, qs_median_three_times, label='Quick Sort Median of 3 Pivot')
    plt.xlabel('Size of Array')
    plt.ylabel('Execution Time (s)')
    plt.title('Execution Time of Merge Sort, Heap Sort, and Quick Sort Median of 3 Pivot')
    plt.legend() 

    # Save the plot in "Homework 2"
    #plt.savefig('Homework 2/Quicksort_RPivot_Comparison.png')
    
    plt.show()

main()