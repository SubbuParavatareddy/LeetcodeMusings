class Solution:
    def isValid(self, s: str) -> bool:
        matching_brackets = {'(' : ')', '{' : '}', '[' : ']'}
        open_paren  = set(['(', '[', '{'])
        stack = []
        for ch in s:
            if ch in open_paren:
                stack.append(ch)
            elif stack and ch == matching_brackets[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []
