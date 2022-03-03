import re

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        expression = '.*'
        for alphabet in s:
            expression += f'{alphabet}.*'
        if re.match(expression, t):
            return True
        else:
            return False
