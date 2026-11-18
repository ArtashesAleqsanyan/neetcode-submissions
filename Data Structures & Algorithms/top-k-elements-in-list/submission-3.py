import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        good_dict = {}
        for num in nums:
            if num not in good_dict:
                good_dict[num] = 0
            good_dict[num] += 1
        top_keys = heapq.nlargest(k, good_dict, key = good_dict.get)
        return top_keys