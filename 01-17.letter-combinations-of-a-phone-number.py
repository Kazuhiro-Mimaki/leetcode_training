class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        hashmap = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(hashmap[digits[0]])
        prev = self.letterCombinations(digits[:-1])
        additional = hashmap[digits[-1]]
        for s in prev:
            for c in additional:
                answer.append(s+c)
        return answer
