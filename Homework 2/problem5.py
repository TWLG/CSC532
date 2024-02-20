import random
import time
from tqdm import tqdm
from quicksort_median3 import quicksort_median
from quick_sort_rpivot import quicksort_rpivot
from random_pivot_quicksort import randomized_quicksort
import matplotlib.pyplot as plt


def main():
    sizes = range(100, 10000, 500)

    qs_random_pivot_times = []
    qs_rpivot_times = []
    qs_median_three_times = [] 

    for size in tqdm(sizes):
        A = [random.randint(-1000, 1000) for i in range(size)]
        
        qs_random_pivot_time = 0
        qs_rpivot_time = 0
        qs_median_three_time = 0

        for _ in range(5):  # run each algorithm 5 times
            
            #TODO imprt p4 algo
            B = list(A)  
            start = time.perf_counter()
            randomized_quicksort(B, 0, len(B) - 1)
            end = time.perf_counter()
            qs_random_pivot_time += end - start


            B = list(A)  
            start = time.perf_counter()
            quicksort_rpivot(B, 0, len(B) - 1)
            end = time.perf_counter()
            qs_rpivot_time += end - start

            B = list(A)
            start = time.perf_counter()
            quicksort_median(B, 0, len(B) - 1)
            end = time.perf_counter()
            qs_median_three_time += end - start

        # average time
        qs_random_pivot_times.append(qs_random_pivot_time / 5)
        qs_rpivot_times.append(qs_rpivot_time / 5)
        qs_median_three_times.append(qs_median_three_time / 5)
    
    plt.plot(sizes, qs_random_pivot_times, label='Random')
    plt.plot(sizes, qs_rpivot_times, label='Rightmost')
    plt.plot(sizes, qs_median_three_times, label='Median')
    plt.xlabel('Size of Array')
    plt.ylabel('Execution Time (s)')
    plt.title('Execution Time of Quicksort: Random, Rightmost, and Median of 3 Pivots')
    plt.legend() 

    # Save the plot in "Homework 2"
    #plt.savefig('Homework 2/Quicksort_RPivot_Comparison.png')
    
    plt.show()

main()