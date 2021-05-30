def max_subarray(numbers):
    """Find the largest sum of any contiguous subarray."""
    best_sum = 0  # or: float('-inf')
    current_sum = 0
    for x in numbers:
        print(x,current_sum)
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum
lis = [-1,2,-1,3]
print(max_subarray(lis))