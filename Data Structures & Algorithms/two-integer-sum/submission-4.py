class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums_dict = {}
        for index, value in enumerate(nums):
            nums_dict[value] = index

        for i in range(n):
            dif = target - nums[i]
            if dif in nums_dict and i != nums_dict[dif]:
                return [i, nums_dict[dif]]


        