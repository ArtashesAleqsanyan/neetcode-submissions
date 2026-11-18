class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        prod = 1
        indxs = []
        for i in range(len(nums)):
            if nums[i] != 0:
                prod *= nums[i]
            else:
                indxs.append(i)
            
        if len(indxs) == 0:
            for i in range(len(nums)):
                r = int(prod / nums[i])
                out.append(r)
        elif len(indxs) == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    out.append(prod)
                else:
                    out.append(0)
        else:
            for i in range(len(nums)):
                out.append(0)    
        return out