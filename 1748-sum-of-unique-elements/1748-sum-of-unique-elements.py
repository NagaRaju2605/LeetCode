class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        count = 0
        for ch in nums:
            if nums.count(ch) == 1:
                count += ch
        return count
        
        