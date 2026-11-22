class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for i, target in enumerate(nums):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] > -target:
                    right -= 1
                elif nums[left] + nums[right] < -target:
                    left += 1
                else:
                    out.append([nums[left], nums[right], target])
                    left += 1   
        seen = set()
        result = []
        for sub in out:
            if tuple(sub) not in seen:
                seen.add(tuple(sub))
                result.append(sub)
        return result