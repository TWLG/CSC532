import math

def max_corssing_sub_array(a, low, mid, high):
    left_sum = -math.inf
    sum = 0
    right_sum = -math.inf
    
    for i in range(mid, low, -1):
        sum = sum + a[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
            
    right_sum = -math.inf
    
    sum = 0
    
    for j in range (mid+1, high):
        sum = sum + a[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    
    return (max_left, max_right, left_sum + right_sum)
    
def max_subarray(a, low, high):
    if high == low:
        return (low, high, a[low])
    else:
        mid = (low + high) // 2
        
        left_low, left_high, left_sum = max_subarray(a, low, mid)
        
        right_low, right_high, right_sum = max_subarray(a, mid + 1, high)

        cross_low, cross_high, cross_sum = max_corssing_sub_array(a, low, mid, high)
        
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else: 
            return (cross_low, cross_high, cross_sum)