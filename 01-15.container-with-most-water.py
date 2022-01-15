class Solution:
    def maxArea(self, height_list: List[int]) -> int:
        maximum = 0
        for i in range(len(height_list)):
            target_range = len(height_list) - (i+1)
            for j in range(i+1, target_range+i+1):
                width = j - i
                # iが始点, jが終点
                if height_list[i] < height_list[j]:
                    height = height_list[i]
                elif height_list[i] >= height_list[j]:
                    height = height_list[j]
                area = height * width
                if area > maximum:
                    maximum = area
        return maximum
