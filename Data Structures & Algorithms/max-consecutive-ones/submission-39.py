class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cons = 0
        curr_max = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr_max = curr_max + 1
                max_cons = max(max_cons,curr_max)
            else:
                curr_max = 0
        
        return max_cons