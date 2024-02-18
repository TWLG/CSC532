"""
FROM THE HW:

Problem 5 (Quicksort w/ Median-of-3 Selected Pivot)
Another way of resolving the “Quicksort worst-case problem” is to 
select the pivot using the Median-of-3 method (described in Problem 7-5).   
In this situation, if the length of the array is greater than 3, we 
choose the pivot by examining three values and choosing the median value as the pivot.   
By tradition, those three values are:
            	A[p]:  	The leftmost value
            	A[r]:   	The rightmost value and
            	A[(p+r)//2]:    	The value at the middle index.
For instance, if our list is [5, 8, 2, 3, 4], we would take the median of 5, 4, and 2.   The median of those three values is 4.	
Then, to use the books partitioning algorithm, we would swap that value with whatever is at A[r] and proceed as normal.
Implement this version of Quicksort and compare its performance with the other two versions of Quicksort on randomly-generated lists and completely sorted lists.  
"""


#! WIP this one isn't working properly yet
def quicksort(m: list[int]):
	assert isinstance(m, list), "Input must be a list"

	length = len(m)
    
	if length < 2:
        # Any list with fewer than 2 elements is always considered sorted
		return m
	
	if length == 2:
		left = m[0]
		right = m[1]
		if left > right:
			m[1] = left
			m[0] = right

		return m

	rightmost = m[length - 1]

	pivot_index = (length - 1) // 2
	pivot = m[pivot_index]

	#* swap that (pivot) value with whatever is at A[rightmost] and proceed as normal

	#? Pivot value -> end index
	m[length - 1] = pivot 
	
	#? Rightmost value -> pivot index
	m[pivot_index] = rightmost

	left_sub_array = m[0:pivot_index]
	right_sub_array = m[pivot_index: length]

	left_sorted = quicksort(left_sub_array)
	right_sorted = quicksort(right_sub_array)

	return left_sorted + right_sorted


test = [5, 8, 2, 3, 4]
print("Before: ", test)
print("After: ", quicksort(test))