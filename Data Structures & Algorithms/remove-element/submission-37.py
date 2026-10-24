class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        while(i < n):
            if nums[i] == val:
                nums[i] = nums[n-1]
                n = n -1
            else:
                i = i +1
        
        return n