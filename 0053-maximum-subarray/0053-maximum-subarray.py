class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 0, 0
        for n in nums:
            tmp = n + curMax
            curMax = max(n + curMax, n + curMin, n)
            curMin = min(n + curMin, tmp, n)
            res = max(curMax, res)
        return res