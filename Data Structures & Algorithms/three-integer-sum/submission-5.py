class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # Now the array is sorted.
        res = []
        prevNum = -10000000000000000000000
        for i in range(len(nums)-2):
            if nums[i] == prevNum:
                continue
            else:
                prevNum = nums[i]

            target = 0 - nums[i]
            ptr1 = i+1
            ptr2 = len(nums)-1
            while True:
                # Index out of bounds
                if ptr1 >= ptr2:
                    break

                print("ptr1: ",ptr1)
                print("ptr2: ",ptr2)

                total = nums[ptr1] + nums[ptr2]
                if total == target:
                    # Found two nums
                    res.append([nums[i],nums[ptr1], nums[ptr2]])
                    prevValue1 = nums[ptr1]
                    prevValue2 = nums[ptr2]
                    while True:
                    
                        if nums[ptr1] == prevValue1:
                            ptr1 += 1
                        if nums[ptr2] == prevValue2:
                            ptr2 -= 1
                        if ptr1 >= ptr2:
                            break
                        if nums[ptr1] != prevValue1 and nums[ptr2] != prevValue2:
                            break
                elif total < target :
                    ptr1 += 1
                else:
                    ptr2 -= 1
                
        return res