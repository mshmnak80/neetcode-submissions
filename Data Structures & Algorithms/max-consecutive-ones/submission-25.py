class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_con = 0
        curr_con = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr_con = curr_con + 1
                if max_con < curr_con:
                    max_con = curr_con
            else:
                curr_con = 0 
        return max_con