class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            max_value = 0
            for k in range(i+1,len(arr)):
                if arr[k] > max_value:
                    max_value = arr[k]
            arr[i] = max_value
        arr[i] = -1
        return arr
        