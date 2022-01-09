class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLen = len(strs[0])
        minIndex = 0
        output = ''
        for i in range(len(strs)):
            if minLen > len(strs[i]):
                minLen = len(strs[i])
                minIndex = i
        minStr = strs[minIndex]
        for i in range(minLen):
            for word in strs:
                if minStr[i] != word[i]:
                    return output
            output += minStr[i]
        return output
