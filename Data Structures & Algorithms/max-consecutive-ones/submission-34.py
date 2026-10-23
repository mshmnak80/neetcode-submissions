class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_max = 0
        max_value = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr_max += 1
                max_value = max(max_value,curr_max)
            else:
                curr_max = 0
        return max_value