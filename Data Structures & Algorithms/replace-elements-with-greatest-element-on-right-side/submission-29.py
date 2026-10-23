class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [0] * len(arr)
        maxright = -1
        n = len(arr)
        for i in range(n-1,-1,-1):
            ans[i] = maxright
            maxright = max(maxright,arr[i])

        return ans


