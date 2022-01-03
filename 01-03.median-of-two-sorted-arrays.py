class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for num in nums2:
            nums1.append(num)
        nums1.sort()
        if len(nums1) % 2 == 0:
            i = len(nums1) // 2
            return (nums1[i-1] + nums1[i]) / 2
        else:
            i = (len(nums1)-1) // 2
            return nums1[i]