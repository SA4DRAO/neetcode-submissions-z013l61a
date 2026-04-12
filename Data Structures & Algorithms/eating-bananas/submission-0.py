class Solution:

    # Time for single array
    def timeForArray(self,piles: List[int], i: int):
        res = 0
        for pile in piles:
            res += (pile + i - 1) // i
        return res

    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search over solution space, which is 0 - h
        l = 1
        r = max(piles)
        ans = r
        
        while l <= r:
            m = l + ((r-l)//2)
            t = self.timeForArray(piles,m)
            print(m)
            # If t is new currMin, then that means I can look for smaller values
            if t <= h:
                r = m - 1
                ans = m
            else:
                # Look at larget values
                l = m + 1
        return ans