class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        prod1 = nums[0]
        n = len(nums)
        for i in range(1, n):
            prod1 *= nums[i]
            prefix.append(prod1)
        suffix = [0] * n
        prod2 = nums[n - 1]
        suffix[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            prod2 *= nums[i]
            suffix[i] = prod2
        out = [0] * n
        out[0] = suffix[1]
        out[n - 1] = prefix[n - 2]
        for i in range(1, n - 1):
            out[i] = prefix[i - 1] * suffix[i + 1]
        return out

        