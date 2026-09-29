class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0 , len(heights)-1
        temp = 0
        max = 0
        total = 0

        while (l<r):
            temp = min(heights[l],heights[r]) 
            max = temp * (r-l)
            if (max > total):
                total = max
            if (heights[l] < heights[r]):
                l+=1
            elif (heights[l] > heights[r]):
                r -= 1
            else:
                l += 1
                r -= 1
        
        return total
