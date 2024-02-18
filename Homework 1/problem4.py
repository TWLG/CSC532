
import time
import random
from tqdm import tqdm
import matplotlib.pyplot as plt

def maximumCrossingSubarrayBook(A, low, mid, high):
    left_sum = float('-inf')
    sum = 0
    for i in range(mid, low - 1, -1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = float('-inf')
    sum = 0
    for j in range(mid + 1, high + 1):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return (max_left, max_right, left_sum + right_sum)

def maximumSubarrayBook(A, low, high):
    if high == low:
        return (low, high, A[low])
    else:
        mid = low + (high - low) // 2
        left_low, left_high, left_sum = maximumSubarrayBook(A, low, mid)
        right_low, right_high, right_sum = maximumSubarrayBook(A, mid + 1, high)
        cross_low, cross_high, cross_sum = maximumCrossingSubarrayBook(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)
    

def maximumSubarrayBruteForce(A):
    max_sum = float('-inf')
    for i in range(len(A)):
        sum = 0
        for j in range(i, len(A)):
            sum += A[j]
            if sum > max_sum:
                max_sum = sum
                max_low = i
                max_high = j
    return (max_low, max_high, max_sum)



def main():
    # Generate random lists of numbers
    sizes = range(100, 10000, 500)
    brute_force_times = []
    book_times = []
    for size in tqdm(sizes, desc='Processing'):
        A = [random.randint(-1000, 1000) for i in range(size)]
        start = time.perf_counter()
        maximumSubarrayBruteForce(A)
        end = time.perf_counter()
        brute_force_times.append(end - start)
        start = time.perf_counter()
        maximumSubarrayBook(A, 0, len(A) - 1)
        end = time.perf_counter()
        book_times.append(end - start)

    # Plot the times
    plt.plot(sizes, brute_force_times, label='Brute Force')
    plt.plot(sizes, book_times, label='Book')
    plt.xlabel('Size of Array')
    plt.ylabel('Execution Time (s)')
    plt.title('Execution Time of Brute Force and Book Algorithms')
    plt.legend()
    plt.show()

main()




