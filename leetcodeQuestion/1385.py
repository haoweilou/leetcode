class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        output = 0
        for num1 in arr1:
            smaller = False
            for num2 in arr2:
                if abs(num1-num2) > d:
                    continue
                else:
                    smaller = True
                    break
            if not smaller:
                output += 1
        return output