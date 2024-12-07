class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        answer = ""
        previous = 0
        for i in spaces:
            answer+=s[previous:i] + " "
            previous = i
        answer+=s[previous:]
        return answer