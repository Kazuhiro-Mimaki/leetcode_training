class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        ans = [[1], [1, 1]]
        for i in range(2, numRows):
            array = [1]
            prev_array = ans[i-1]
            for index, j in enumerate(prev_array):
                if index == len(prev_array)-1:
                    array.append(1)
                    ans.append(array)
                    continue
                num = prev_array[index] + prev_array[index+1]
                array.append(num)
        return ans
