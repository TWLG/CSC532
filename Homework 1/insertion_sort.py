def insertion_sort(arr):
    for curr_index in range(1, len(arr)):
        curr_value = arr[curr_index]
        comparison_index = curr_index - 1
        
        while comparison_index >= 0 and curr_value < arr[comparison_index]:
            arr[comparison_index + 1] = arr[comparison_index]
            comparison_index -= 1

        arr[comparison_index + 1] = curr_value
    
    return arr

#spareflame