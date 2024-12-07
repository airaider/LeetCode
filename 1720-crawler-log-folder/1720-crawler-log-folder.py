class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = 0
        for log in logs:
            if log == "../" and stack > 0:
                stack -= 1
            elif log not in {"../", "./"}:
                stack += 1
        return stack
