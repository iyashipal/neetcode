class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        if k<=0:
            return res
        
        count = {} #hashmap to count number of times a value repeats
        #frequency array, same length as nums (max freq possible is len(nums) so we can use that as index of freq array), then put list in each index including values that are of that particular frequency
        freq = [[] for i in range (len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        #now add these counted values to freq array
        for n,c in count.items():
            # n - value, c - it's frequency/count
            freq[c].append(n)

        #now add k most frequent elements in the result array
        for i in range(len(freq)-1, 0 , -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

