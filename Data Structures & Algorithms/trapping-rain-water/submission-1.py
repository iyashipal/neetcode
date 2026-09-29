class Solution:
    def trap(self, height: List[int]) -> int:
        total  = 0
        pref = [0] * len(height)
        suff = [0] * len(height)
        temp = height[0]

        for i in range(0, len(height)):
            if height[i] > temp:
                temp = height[i]
            pref[i] = temp
        
        temp = height[-1] 
        
        for i in range (len(height)-1,-1, -1):
            if height[i] > temp:
                temp = height[i]
            suff[i] = temp

        for i in range (0, len(height)-1):
            total += min(pref[i],suff[i]) - height[i]

        return total
        