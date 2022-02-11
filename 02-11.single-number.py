class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_map = {}
        ans = nums[0]
        for n in nums:
            if n in hash_map:
                hash_map[n] += 1
            else:
                hash_map[n] = 1
        for k,v in hash_map.items():
            if v == 1:
                return k