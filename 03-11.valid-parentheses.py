class Solution:
    def isValid(self, s: str) -> bool:
        left = set('([{')
        right = set(')]}')
        check = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in s:
            if i in left:
                stack.append(i)
            if i in right:
                if not stack:
                    return False
                elif stack.pop() != check[i]:
                    return False
                else:
                    continue
        return not stack
