class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        def calculateOperations(nums, target):
            operations = 0
            for num in nums:
                operations += (num - 1) // target
            return operations
    
        left = 1
        right = max(nums)
        
        while left < right:
            mid = (left + right) // 2
            
            operations = calculateOperations(nums, mid)
            
            if operations <= maxOperations:
                right = mid
            else:
                left = mid + 1
        
        return left



        