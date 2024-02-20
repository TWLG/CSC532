from quick_sort_rpivot import partition

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
def quicksort_median_pivot(array: list[int], pivot: int, rightmost: int):
	assert isinstance(array, list), "Input must be a list"

	length = len(array)
    
	if length < 2:
        # Any list with fewer than 2 elements is always considered sorted
		return array
	
	if length == 2:
		left = array[0]
		right = array[1]
		if left > right:
			array[1] = left
			array[0] = right

		return array

	if pivot < rightmost:
		result = partition(array, pivot, rightmost)
		quicksort_median_pivot(array, pivot, result - 1)
		quicksort_median_pivot(array, result + 1, rightmost)