class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        allset = set(range(len(nums)+1))
        givenset = set(nums)
        return list(allset - givenset)[0]