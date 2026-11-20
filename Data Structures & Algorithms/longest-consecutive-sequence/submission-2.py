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
        cons = [[start[i]] for i in range(len(start))]
        for i in range(len(start)):
            j = 1
            while start[i] + j in nums_set:
                cons[i].append(start[i] + j)
                j += 1
        longest = 0
        for i in range(len(start)):
            longest = max(longest, len(cons[i]))
        return longest
        