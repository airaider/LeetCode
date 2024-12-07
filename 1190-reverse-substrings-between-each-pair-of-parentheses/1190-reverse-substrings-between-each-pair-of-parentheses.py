class Solution:
    def reverseParentheses(self, s: str) -> str:

        stack = []
        current = []

        for c in s:
            if c == "(":
                stack.append(current)
                current = []
            elif c == ")":
                a = stack.pop()
                current.reverse()
                current=a+current
            else:
                current.append(c)
        return ''.join(current)
            

        