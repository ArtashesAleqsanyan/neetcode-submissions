class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            tuple_count = tuple(count)
            if tuple_count not in anagram_dict:
                anagram_dict[tuple_count] = []
            anagram_dict[tuple_count].append(s)
        return list(anagram_dict.values())

