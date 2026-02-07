class Solution:
    def isValid(self, s: str) -> bool:
        valid_pairs = { '(' : ')', '{' : '}', '[' : ']' }
        open_paren = set(['(', '{', '['])
        my_stack = []

        for ch in s:
            if ch in open_paren:
                my_stack.append(ch)
            elif my_stack and ch == valid_pairs[my_stack[-1]]:
                my_stack.pop()
            else:
                return False
        return my_stack == []