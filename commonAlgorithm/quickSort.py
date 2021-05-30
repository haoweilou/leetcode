from typing import List


def quickSort(nums: List,left: int, right: int):
    if left < right:
        pi = partition(nums,left,right)
        quickSort(nums,left,pi-1)
        quickSort(nums,pi+1,right)

def partition(nums: List, left:int,right:int):
    leftWall = left
    pivot = nums[right]

    for j in range(left,right):
        if nums[j] <= pivot:
            nums[j],nums[leftWall] = nums[leftWall],nums[j]
            leftWall += 1
    nums[right],nums[leftWall] = nums[leftWall],nums[right]
    return leftWall

n = [3,4,1,2,5,7,2,6]
quickSort(n,0,7)
print(n)
