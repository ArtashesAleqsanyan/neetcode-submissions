class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for x in s:
            if x.isalnum():
                s1 += x.lower()
        n = len(s1)
        for i in range(n // 2):
            if s1[i] != s1[n - 1 - i]:
                return False
        return True