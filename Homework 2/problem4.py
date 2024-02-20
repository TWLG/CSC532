from merge_sort import merge_sort
from heap_sort import heap_sort
from quick_sort_rpivot import partition
from random_pivot_quicksort import random_pivot_quicksort
import time
import matplotlib.pyplot as plt


def test_sorted_arrays(sizes):
    heap_sort_times = []
    merge_sort_times = []
    quicksort_random_pivot_times = []

    for size in sizes:
        # Generate already sorted array
        A = list(range(size))

        # Test Heap Sort
        heap_sorted = list(A)
        start_time = time.perf_counter()
        heap_sort(heap_sorted)
        end_time = time.perf_counter()
        heap_sort_times.append(end_time - start_time)

        # Test Merge Sort
        merge_sorted = list(A)
        start_time = time.perf_counter()
        merge_sort(merge_sorted, 0, len(merge_sorted) - 1)
        end_time = time.perf_counter()
        merge_sort_times.append(end_time - start_time)

        # Test Quicksort with randomly selected pivot
        quicksort_random_pivot = list(A)
        start_time = time.perf_counter()
        random_pivot_quicksort(quicksort_random_pivot, 0, len(quicksort_random_pivot) - 1)
        end_time = time.perf_counter()
        quicksort_random_pivot_times.append(end_time - start_time)

    print(len(heap_sort_times), len(merge_sort_times), len(quicksort_random_pivot_times))
    return heap_sort_times, merge_sort_times, quicksort_random_pivot_times


def plot_sorted_arrays(sizes, heap_sort_times, merge_sort_times, quicksort_random_pivot_times):
    plt.plot(sizes, heap_sort_times, label='Heap Sort')
    plt.plot(sizes, merge_sort_times, label='Merge Sort')
    plt.plot(sizes, quicksort_random_pivot_times, label='Quicksort Random Pivot')
    plt.xlabel('Size of Array')
    plt.ylabel('Execution Time (s)')
    plt.title('Execution Time of Sorting Algorithms on Already Sorted Arrays')
    plt.legend()
    plt.grid(True)
    plt.show()

# Test and plot
sizes = range(100, 10000, 500)
heap_sort_times, merge_sort_times, quicksort_random_pivot_times = test_sorted_arrays(sizes)
plot_sorted_arrays(sizes, heap_sort_times, merge_sort_times, quicksort_random_pivot_times)
