class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_pattern_id = 1
        s_hashmap = {}
        for ss in s:
            if s_hashmap.get(ss) is None:
                s_hashmap[ss] = s_pattern_id
                s_pattern_id += 1
        s_output = ''
        for ss in s:
            s_output += str(s_hashmap[ss])

        t_pattern_id = 1
        t_hashmap = {}
        for tt in t:
            if t_hashmap.get(tt) is None:
                t_hashmap[tt] = t_pattern_id
                t_pattern_id += 1
        t_output = ''
        for tt in t:
            t_output += str(t_hashmap[tt])
        
        return s_output == t_output