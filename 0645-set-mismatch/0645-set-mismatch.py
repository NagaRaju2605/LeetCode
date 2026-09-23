class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1

        dulpicate = 0
        missing = 0
        for i in range(1,len(nums) + 1):
            if d.get(i,0) == 2:
                duplicate = i
            elif d.get(i,0) == 0:
                missing = i
        return(duplicate, missing)

        
        