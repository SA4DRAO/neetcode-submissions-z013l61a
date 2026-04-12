class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Assume no zeros
        leftValues = []
        rightValues = []
        for i in range(len(nums)):
            # Left values is empty -> first elem, empty array
            if len(leftValues) == 0:
                leftValues.append([])
                print("INSERTED FIRST VALUE")
                print(leftValues)
                continue
            else:
                leftValues.append(leftValues[i-1] + [nums[i-1]])
                
        for i in range(len(nums)):
            # Right values is empty -> last elem, empty array
            if len(rightValues) == 0:
                rightValues.append([])
                continue
            else:
                rightValues.append(rightValues[i-1] + [nums[len(nums)-i]])
        print(leftValues)
        rightValues.reverse()
        print(rightValues)

        final = []
        for i in range(len(nums)):
            left = leftValues[i]
            right = rightValues[i]
            # Now I need to multiply both
            total = left + right
            res = 1
            for element in total:
                res *= element
            final.append(res)
        return final 