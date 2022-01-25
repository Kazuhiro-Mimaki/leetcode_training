class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        curr = []
        for i in range(len(nums)):
            curr.append(nums[i])
            if len(nums) == 0:
                output.append(curr)
                curr = []
                return
            self.permute(nums[:i]+nums[i:])
