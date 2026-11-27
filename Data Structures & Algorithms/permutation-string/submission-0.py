class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        left = 0
        d1 = {}
        d2 = {}
        for i in range(n1):
            d1[s1[i]] = 1 + d1.get(s1[i], 0)
            d2[s2[i]] = 1 + d2.get(s2[i], 0)
        for right in range(n1, n2):
            if d1 == d2:
                return True
            d2[s2[right]] = 1 + d2.get(s2[right], 0)
            d2[s2[left]] -= 1
            if d2[s2[left]] == 0:
                del d2[s2[left]]
            left += 1
        return d1 == d2
