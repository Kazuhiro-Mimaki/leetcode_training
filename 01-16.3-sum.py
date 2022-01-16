class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        sorted_list = sorted([nums[i], nums[j], nums[k]])
                        if not sorted_list in output:
                            output.append(sorted_list)
        return output