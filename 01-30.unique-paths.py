class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        min_num = min(m, n)
        if min_num == 1:
            return 1
        denominator = m+n-2
        numerator = min_num-1
        for num in range(min_num-2):
            denominator *= (m+n-2 - num-1)
        for num in range(min_num-2):
            numerator *= (min_num-1 - num-1)
        return denominator // numerator
