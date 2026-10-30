class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        for x in range(len(s2) - len(s1) + 1):
            count = {}

            for y in range(len(s1)):
                count[s2[x+y]] = count.get(s2[x+y], 0) + 1

            if count == {c: s1.count(c) for c in set(s1)}:
                return True

        return False