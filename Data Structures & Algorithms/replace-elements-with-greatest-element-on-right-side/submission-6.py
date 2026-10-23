class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            #find max value
            max_value = 0
            for k in (range(i+1,len(arr))):
                if max_value < arr[k] :
                    max_value = arr[k]
            arr[i] = max_value
        arr[-1] = -1
        return arr