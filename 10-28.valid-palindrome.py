class Solution:
    def isPalindrome(self, s: str) -> bool:
        ext_s = re.sub('[^a-zA-Z0-9]+', '', s).lower()
        reversed_s = ext_s[::-1]
        return ext_s == reversed_s
