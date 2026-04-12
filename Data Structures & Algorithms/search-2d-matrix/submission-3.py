class Solution:
    def searchMatrix(self, nums: List[List[int]], target: int) -> bool:
        # Search column
        left = 0
        right = len(nums)-1
        while left <= right:
            print("LEFT:", left)
            print("Right:", right)

            mid = left + ((right - left) // 2)
            print("MID:",mid)
            if nums[mid][0] < target:
                left = mid + 1
            
            elif nums[mid][0] > target:
                right = mid -1
            
            else:
                return True
        # Now left and right are equal to mid, which will be the row in which it is present
        l = 0
        r = len(nums[0])-1
        while l <= r:
            
            print("LEFT:", l)
            print("Right:", r)

            m = l + ((r-l)//2)
            print("MID2: ", m)
            if nums[right][m] < target:
                l = m + 1

            elif nums[right][m] > target:
                r = m - 1
            
            else:
                return True
        return False