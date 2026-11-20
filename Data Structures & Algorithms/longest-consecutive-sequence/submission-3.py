class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        start = []
        for el in nums_set:
            if el + 1 in nums_set and el - 1 not in nums_set:
                start.append(el)
        if not start:
            return 1
        counts = [1] * len(start)
        for i in range(len(start)):
            j = 1
            while start[i] + j in nums_set:
                counts[i] += 1
                j += 1              
        longest = max(counts)
        return longest