class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        total_sum = 0
        answer_list = []
        banned_set = set(banned)
        for i in range(1, n+1):
            if i not in banned_set and i+total_sum <= maxSum:
                answer_list.append(i)
                total_sum += i
            if total_sum > maxSum:
                break
        return len(answer_list)
