class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = { '(' : ')', '{' : '}', '[' : ']' }
        open_par = set(['(', '[', '{'])
        stack = []
        for ch in s:
            if ch in open_par:
                stack.append(ch)
            elif stack and ch == bracket_map[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []