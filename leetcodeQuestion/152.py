from typing import List
'''
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n0 = nums[0]
        prevMax = n0
        prevMin = n0
        currMax = n0 
        currMin = n0
        output = n0
        for i in nums[1:]:
            currMax = max(max(prevMax*i,prevMin*i),i)
            currMin = min(min(prevMax*i,prevMin*i),i)
            
            prevMax = currMax
            prevMin = currMin
            
            output = max(prevMax,output)
        return output