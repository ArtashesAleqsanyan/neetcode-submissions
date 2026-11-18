class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in range(len(strs)):
            width = str(len(strs[i]))
            result = result + width + "#" + strs[i] 
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            n = ""
            for j in range(i, len(s)):
                if s[j].isdigit():
                    n = n + s[j] 
                else: break
            num = int(n)
            l = len(n)
            word = ""
            for k in range((i + l + 1), (i + num + l + 1)): 
                word = word + s[k]
            result.append(word)
            i += 1 + num + l
        return result

