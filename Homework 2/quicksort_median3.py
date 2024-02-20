def swapget_median(arr, p, r):
    median = (p + r) // 2
    low = arr[p]
    high = arr[r]
    mid = arr[median]
    if low > high and low < mid or low < high and low > mid:
        arr[p], arr[r] = arr[r], arr[p]
    elif mid > high and mid < low or mid < high and mid > low:
        arr[median], arr[r] = arr[r], arr[median]
    return arr[r]


def partition_median(arr, low, high):
    pivot = swapget_median(arr, low, high)
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1 

def quicksort_median(arr, low, high):
    if low < high:
        p = partition_median(arr, low, high)
        if p is None:
            return
        quicksort_median(arr, low, p - 1)
        quicksort_median(arr, p + 1, high)

def main():
    arr = [3, 2, 1, 5, 4,7]
    quicksort_median(arr, 0, len(arr) - 1)


main()