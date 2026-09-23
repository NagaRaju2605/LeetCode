class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        result = []
        d = {}
        for i in nums:
            if i in d:
                result.append(i)
            else:
                d[i] = 1
        
        return result
