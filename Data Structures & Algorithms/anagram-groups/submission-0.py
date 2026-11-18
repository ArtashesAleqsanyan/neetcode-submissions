class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in anagram_dict:
                anagram_dict[sorted_s] = []
            anagram_dict[sorted_s].append(s)
        anagram_list = list(anagram_dict.values())
        return anagram_list

