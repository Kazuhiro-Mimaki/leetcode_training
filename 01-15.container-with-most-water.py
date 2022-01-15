class Solution:
    def maxArea(self, height_list: List[int]) -> int:
        maximum = 0
        left, right = 0, len(height_list) - 1
        while left < right:
            height = min(height_list[left], height_list[right])
            width = right - left
            area = height * width
            if maximum < area:
                maximum = area
            if height_list[left] < height_list[right]:
                left += 1
            elif height_list[left] >= height_list[right]:
                right -= 1
        return maximum
