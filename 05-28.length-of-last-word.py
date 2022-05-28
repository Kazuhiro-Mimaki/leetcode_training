class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wordlist = s.split()
        lastword = wordlist[len(wordlist)-1]
        return len(lastword)