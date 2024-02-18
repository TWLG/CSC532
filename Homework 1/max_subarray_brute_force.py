def max_subarray_bruteforce(number_array):
    length_of_array = len(number_array)
    if length_of_array == 0:
        return 0, []

    max_sum = float('-inf')
    start_index = end_index = 0

    for current_index_outer in range(length_of_array):
        current_sum = 0
        for current_index_inner in range(current_index_outer, length_of_array):
            current_sum += number_array[current_index_inner]
            if current_sum > max_sum:
                max_sum = current_sum
                start_index = current_index_outer
                end_index = current_index_inner

    return max_sum, number_array[start_index:end_index + 1]