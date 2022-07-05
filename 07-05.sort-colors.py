class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        b0, b1, b2 = 0, 0, 0
        for num in nums:
            if num == 0:
                b0 += 1
            elif num == 1:
                b1 += 1
            elif num == 2:
                b2 += 1
        nums[:b0] = [0]*b0
        nums[b0:b0+b1] = [1]*b1
        nums[b0+b1:] = [2]*b2
        return nums