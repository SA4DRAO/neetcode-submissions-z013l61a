class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [None]*len(temperatures)

        for index, temp in enumerate(temperatures):
            if not stack:
                stack.append([index,temp])
            else:
                while(stack[-1][1] < temp or not stack):
                    res[stack[-1][0]] = index - stack[-1][0]
                    stack.pop()
                    if not stack:
                        break 
                stack.append([index,temp])

        if stack:
            for index, val in stack:
                res[index] = 0
        return res

