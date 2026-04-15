class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        maxvol = 0
        while left < right:
            maxvol = max(maxvol, (right - left) * min(heights[left], heights[right]))
            if heights[right] < heights[left]:
                right-=1
            else:
                left+=1
            

        return maxvol