class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cons_ones = 0
        max_cons = 0
        for i,num in enumerate(nums):
            if num == 1:
                cons_ones += 1
                max_cons = max(max_cons,cons_ones)
            else:
                cons_ones = 0
        
        return max_cons
