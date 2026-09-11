class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #METHOD 1: 
        #Brute force: check every pair
        #Time complexity: O(n^2), space complexity: O(1)
        #for i in range(0,len(nums)-1):
        #    for j in range(i+1, len(nums)):
        #        if(nums[i]+nums[j]==target):
        #            return [i,j];


        #METHOD 2: Sorting
        #copy = nums #cannot use this coz this doesn't make a copy, it just points tothe same array
        # Time complexity O(nlogn) space complexity O(n)
        #copy = nums.copy()
        #copy.sort()
        #i=0; j=len(copy)-1;
        #while i<j:
        #    sum = copy[i]+copy[j];
        #    if target == sum:
        #        return [nums.index(copy[i]), nums.index(copy[j])]
        #    elif target < sum:
        #        j-=1
        #    else:
        #        i+=1
        #return[]
            


        #METHOD 3: Use hashmap, for each index diff = target - nums[i] check if diff exists in hashmap, or store (value, index) in hashmap
        #Time complexity: O(n) space complexity O(n)
        hashmap= {nums[0]:0}
        for i in range(1,len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff],i]
            hashmap[nums[i]] = i
        return []
        




        

