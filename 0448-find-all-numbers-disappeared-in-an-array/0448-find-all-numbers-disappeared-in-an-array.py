class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        result = []
        s = set(nums)
        for i in range(1,len(nums) + 1):
            if i not in s:
                result.append(i)
        return result
        