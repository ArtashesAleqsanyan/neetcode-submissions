class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s1 = [0] * 26
        max_l = 0
        left = 0
        for i in range(k + 1):
            s1[ord(s[i]) - ord('A')] += 1
        i = k + 1
        while i < len(s):
            if sum(s1) - max(s1) <= k:
                s1[ord(s[i]) - ord('A')] += 1
                i += 1
            else:
                s1[ord(s[left]) - ord('A')] -= 1
                left += 1
                s1[ord(s[i]) - ord('A')] += 1
                i += 1
            max_l = max(max_l, k + max(s1))
        if sum(s1) - max(s1) <= k:
            return sum(s1)
        return max_l