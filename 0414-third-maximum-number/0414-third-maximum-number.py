class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        d = {}
        for i in nums:
            d[i] = 1

        nums = list(d.keys())
        nums.sort(reverse=True)
        if len(nums) < 3:
            return nums[0]

        return nums[2]