class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        s1 = set()
        i = 0
        while i < len(s):
            while i < len(s) and s[i] not in s1:
                s1.add(s[i])
                i += 1
            max_len = max(max_len, len(s1))
            while i < len(s) and s[i] in s1:
                s1.remove(s[left])
                left += 1
            if i < len(s):
                s1.add(s[i])
            i += 1
        return max_len
