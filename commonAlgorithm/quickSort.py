import random
from typing import List
#cleanest method
def quickSort(nums:List):
    n = len(nums)
    if n <= 1:
        return nums
    pivot = nums.pop()
    smaller = []
    greater = []
    for num in nums:
        if num < pivot:
            smaller.append(num)
        else:
            greater.append(num)
    return quickSort(smaller) + [pivot] + quickSort(greater)


n = [random.randint(0,100) for _ in range(10000)]
print(n)
print(quickSort(n))
