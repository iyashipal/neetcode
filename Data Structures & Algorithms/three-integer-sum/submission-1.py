class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        i , j, k = 0, 1 , 2
        while i <= len(nums)-3:
            j = i+1
            k= len(nums) - 1
            while j < k:
                if(nums[i]+nums[j]+nums[k] == 0):
                    result.append([nums[i],nums[j],nums[k]])
                    
                    while (j < k  and nums[j]==nums[j+1] ):
                        j+=1
                    while (k>j and nums[k]==nums[k-1] ):
                        k-=1
                    j+=1
                    k-=1
                elif(nums[i]+nums[j]+nums[k] < 0):
                    
                    while (j < k  and nums[j]==nums[j+1] ):
                        j+=1
                    j+=1
                else:
                    
                    while (k >j   and nums[k]==nums[k-1] ):
                        k-=1
                    k-=1
            
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i+=1

            i+=1
        return result