class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        numbers = set(arr)

        if arr.count(0) > 1:
            return True
        
        for i in arr:
            if i != 0 and i*2 in numbers: return True
        return False