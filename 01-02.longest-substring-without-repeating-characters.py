class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        count = 0
        substring = ''
        hashmap = {'substring': substring, 'count': count}
        for split_str in s:
            if split_str in substring and hashmap['count'] <= count:
                hashmap['substring'] = substring
                hashmap['count'] = count
                substring = split_str
                count = 1
            else:
                substring += split_str
                count += 1
        return hashmap['count']
