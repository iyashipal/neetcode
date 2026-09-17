class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #sort the array
        #Time complexity: O(n log n) 
        #Space complexity: O(1)
        ''' nums.sort()
        count= 0
        max = 1
        for i in range(len(nums)-1):
            if (nums[i]==nums[i+1] or nums[i]+1==nums[i+1]):
                count+=1
                max = count
            else:
                count=1
        return max '''

        #using hashset
        seq = set(nums)
        count = 0
        max = 0
        for temp in nums:
            if (temp-1) not in seq: #temp is start of sequence
                count = 1
                while(temp+1) in seq: #check if next value exists 
                    count+=1
                    temp+=1
                if(count>max):
                    max= count
            count = 1
        return max