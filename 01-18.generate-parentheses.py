class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        ans = []

        def recursion(S=[], left=0, right=0):
            if len(S) == 2*n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                recursion(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                recursion(S, left, right+1)
                S.pop()
        recursion()
        return ans
