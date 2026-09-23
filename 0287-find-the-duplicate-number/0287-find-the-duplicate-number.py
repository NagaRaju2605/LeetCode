class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        result = []
        d = {}
        for i in nums:
            if i in d:
                return i
            d[i] = 1
        return result
        