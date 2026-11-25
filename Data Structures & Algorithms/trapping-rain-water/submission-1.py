class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        total = 0
        n = len(height)
        r_max = [0] * n
        r_max[n - 1] = height[n - 1]
        for i in range(n - 2, 0, -1):
            r_max[i] = max(r_max[i + 1], height[i])
        l_max = [0] * n
        l_max[0] = height[0]
        for i in range(1, n):
            l_max[i] = max(l_max[i - 1], height[i])
        for i in range(1, n - 1):
            val = min(l_max[i - 1], r_max[i + 1]) - height[i]
            if val > 0:
                total += val
        return total   