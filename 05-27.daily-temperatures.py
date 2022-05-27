class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # ans = [0] * len(temperatures)
        # for i in range(len(temperatures)):
        #     for j in range(i, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             ans[i] = j - i 
        #             break
        # return ans
        ans = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)                    
        return ans
