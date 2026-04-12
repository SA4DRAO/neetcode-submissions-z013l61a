class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Assume no zeros
        leftValues = []
        rightValues = []
        for i in range(len(nums)):
            # Left values is empty -> first elem, empty array
            if len(leftValues) == 0:
                leftValues.append([])
                continue
            else:
                if leftValues[i-1] == []:
                    # Second index, just add elem itself
                    leftValues.append(nums[i-1])
                else:
                    leftValues.append(leftValues[i-1] * nums[i-1])
                
        for i in range(len(nums)):
            # Right values is empty -> last elem, empty array
            if len(rightValues) == 0:
                rightValues.append([])
                continue
            else:
                if rightValues[i-1] == []:
                    rightValues.append(nums[len(nums)-i])
                else:
                    rightValues.append(rightValues[i-1] * nums[len(nums)-i])

        rightValues.reverse()
        print(leftValues)
        print(rightValues)
        final = []
        for i in range(len(nums)):
            if leftValues[i] == []:
                total = rightValues[i]
            elif rightValues[i] == []:
                total = leftValues[i]
            else:
                total = leftValues[i] * rightValues[i]
            final.append(total)
        return final 