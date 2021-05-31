import random
from typing import List

#cleanest method
'''
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
'''
#using partition
def quickSort(nums:List,left:int,right:int):
    if left >= right:
        return
    piviotIndex = partition(nums,left,right)
    quickSort(nums,left,piviotIndex-1)
    quickSort(nums,piviotIndex+1,right)

def partition(nums:List,left:int,right:int):
    pivot = nums[right]
    i = left - 1
    while left <= right:
        if nums[left] < pivot:
            i+=1
            nums[left],nums[i] = nums[i],nums[left]
        left += 1
    nums[i+1],nums[right] = nums[right],nums[i+1]
    return i+1


n = [random.randint(0,100) for _ in range(10000)]
print(n)
quickSort(n,0,len(n)-1)
print(n)
