class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) #type of dictionary: creates an empty list for any new or missing key you try to access
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count [ord(c) - ord("a")] +=1
            result[tuple(count)].append(s)

        return list(result.values())