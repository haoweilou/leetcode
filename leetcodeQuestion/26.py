'''
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return
        currNum = nums[0]
        j = 1
        for i in range(1,n):
            if nums[i] != currNum:
                nums[j] = nums[i]
                currNum = nums[j]
                j+=1
        while(len(nums) > j):
            nums.pop()