class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_hashmap = {}
        for i in s:
            if i in s_hashmap:
                s_hashmap[i] += 1
            else:
                s_hashmap[i] = 0

        t_hashmap = {}
        for i in t:
            if i in t_hashmap:
                t_hashmap[i] += 1
            else:
                t_hashmap[i] = 0

        for i in t:
            if s_hashmap.get(i) != t_hashmap.get(i):
                return i
