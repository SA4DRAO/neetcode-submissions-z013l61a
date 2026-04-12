class Solution:
    def trap(self, height: List[int]) -> int:
        maxOnRight = []
        maxOnLeft = []

        for index,i in enumerate(height):
            if index == 0:
                maxOnLeft.append(0)
                continue
            # Build maxOnLeft
            maxOnLeft.append(max(maxOnLeft[index-1], height[index-1]))

        height.reverse()
        for index,i in enumerate(height):
            if index == 0:
                maxOnRight.append(0)
                continue
            # Build maxOnLeft
            maxOnRight.append(max(maxOnRight[index-1], height[index-1]))
        maxOnRight.reverse()
        height.reverse()
        print(height)
        print(maxOnLeft)
        print(maxOnRight)
        
        maxarea = 0

        for i in range(len(height)):
            if min(maxOnLeft[i], maxOnRight[i]) > height[i]:
                maxarea += min(maxOnLeft[i], maxOnRight[i]) - height[i]
        return maxarea