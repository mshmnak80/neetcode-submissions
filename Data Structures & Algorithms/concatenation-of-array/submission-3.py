class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ans = []

        ans.extend(nums)
        ans.extend(nums)
        # for index in range(2):
        #     for num in nums:
        #         ans.append(num)

        return ans
