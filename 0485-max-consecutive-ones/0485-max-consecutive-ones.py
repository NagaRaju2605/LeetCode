class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0
        maximum = 0
        for i in nums:
            if i == 1:
                count += 1
                maximum = max(maximum,count)
            else:
                count = 0
        return maximum
               
        
        
 
              
            
        