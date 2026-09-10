class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #METHOD 1:
        # Brute force method: check every element against every other element in the array
        # Time complexity O(n^2), space complexity : 0
        #for i in range(0,len(nums)-1):
        #    for j in range (i+1,len(nums)):
        #        if nums[i] == nums[j]:
        #            return True;
        #return False;
        
        #METHOD 2:
        # Sort array first and then compare pairs from beginning to end.
        # Time complexity O(nlogn) : O(n) - for comparing and O(logn) - for sorting, space complexity : 0
        #nums.sort;
        #for i in range (0,len(nums)-1):
        #    if(nums[i]) == nums[i+1]:
        #        return True;
        #return False;


        #METHOD 3:
        # Use Hashset to store the values and compare. Uses space but most efficient. 
        # Time complexity O(n) and space complexity O(n)
        hashset = set()
        for n in nums:
            if n in hashset:
                return True;
            hashset.add(n);
        return False;