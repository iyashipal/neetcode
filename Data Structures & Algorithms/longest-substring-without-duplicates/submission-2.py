class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #SLIDING WINDOW
        charSet = set()
        left = 0
        res = 0
        for right in range (len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left+=1
            charSet.add(s[right])
            res = max(res, right-left+1)
        return res
        
        
        #ONLY WORKS FOR ALPHABETS
        # arr = [0] * 26
        # count, max = 0 , 0
        # l = len(s)
        # for x in range (0,l):
        #     if count > max:
        #         max = count
        #     count = 0
        #     for temp in range (x,l):
        #         if arr[ord(s[temp])-97] == 0:
        #             count +=1
        #             arr[ord(s[temp])-97] = 1
        #         else:
        #             arr = [0] * 26
        #             break;
        # return max

            