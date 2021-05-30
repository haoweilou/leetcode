class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        n = len(nums)
        right = n-1
        for i in range(n):
            first = nums[i]
            if(i != 0 and first==nums[i-1]):
                continue
            j = i + 1
            k = n - 1
            while(j<k):
                if(nums[j]+nums[k]==first*-1):
                    output.append([first,nums[j],nums[k]])
                    j += 1
                    while(j<n and nums[j-1]==nums[j]):
                        j += 1
                elif(nums[j]+nums[k] <=first*-1):
                    j += 1
                else:
                    k -= 1
        return output
                