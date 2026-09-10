class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False;
        
        #Use dictionary to keep count
        count = {} 

        for x in s:
            count[x] = count.get(x,0) + 1;

        for x in t:
            count[x] = count.get(x,0) - 1;

        if all(value==0 for value in count.values()):
            return True;
        else:
            return False;