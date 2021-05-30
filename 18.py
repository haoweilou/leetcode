#Simplest approach not intelligient
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        snums = sorted(nums)#nlog(n)
        n = len(snums)
        output = []
        for i in range(n):
            numi = snums[i]
            for j in range(i+1,n):
                numj = snums[j]
                desire = target - numi - numj
                twosums = self.twoSum(snums[j+1:],desire)
                for combines in twosums:
                    item = [numi,numj]+combines
                    if item not in output:
                        output.append(item)
        return output
            
    def twoSum(self,nums:List[int], target: int) -> List[List[int]]:
        n = len(nums)
        output = []
        l = 0
        r = n-1
        while l < r:
            left = nums[l]
            right = nums[r]
            value = left + right      
            if value < target or (l>0 and nums[l] == nums[l-1]):
                l += 1
            elif value > target  or (r<n-1 and nums[r] == nums[r+1]):
                r -= 1
            else:
                output.append([nums[l],nums[r]])
                l += 1
                r -= 1
                
        return output

#Can solve any combination
class Solution1:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums: List[int], target: int, k:int) -> List[List[int]]:
            output = []
            n = len(nums)
            if len(nums) == 0 or nums[0]*k > target or nums[n-1]*k < target:
                return output
            if k == 2:
                return twoSum(nums,target)
            for i in range(n):
                numi = nums[i]
                results = kSum(nums[i+1:],target-numi,k-1)
                if i > 0 and numi == nums[i-1]:
                    continue
                for result in results:
                    output.append([numi]+result)
            return output
        
        def twoSum(nums:List[int], target: int) -> List[List[int]]:
            n = len(nums)
            output = []
            l = 0
            r = n-1
            while l < r:
                left = nums[l]
                right = nums[r]
                value = left + right      
                if value < target or (l>0 and nums[l] == nums[l-1]):
                    l += 1
                elif value > target  or (r<n-1 and nums[r] == nums[r+1]):
                    r -= 1
                else:
                    output.append([nums[l],nums[r]])
                    l += 1
                    r -= 1           
            return output
        
        sortedNums = sorted(nums)
        return kSum(sortedNums,target,8)

s = Solution1()
print(s.fourSum([-1,-2,-3,-4,5,6,7,8,9,100,34,1],42))
