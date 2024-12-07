class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set()
        for i in allowed:
            allowed_set.add(i)
        answer=len(words)
        for word in words:
            for i in word:
                if i not in allowed_set:
                    answer -=1
                    break
        return answer
        