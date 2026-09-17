class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        pref = [1]*len(nums) #to store prefix products
        suff = [1]*len(nums) #to store suffix products
        res = [1]*len(nums) #result array
        for i in range (len(nums)):
            pref[i] = prod
            prod *= nums[i]
        
        prod = 1

        for i in range (len(nums)-1, -1 , -1):
            suff[i] = prod
            prod *= nums[i]
        
        for i in range (len(nums)):
            res[i] = pref[i]*suff[i]
        
        return res