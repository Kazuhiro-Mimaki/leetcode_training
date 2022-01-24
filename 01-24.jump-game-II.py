class Solution:
    def jump(self, nums: List[int]) -> int:
        jmps = [math.inf for _ in range(len(nums))]
        jmps[0] = 0
        for i in range(len(nums) - 1):
            farthest = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, farthest + 1):
                jmps[j] = min(jmps[j], jmps[i] + 1)
        return jmps[-1]
