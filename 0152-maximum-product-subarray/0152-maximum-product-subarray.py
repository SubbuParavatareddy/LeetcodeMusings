class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1, 1
        for i in nums:
            tmp = i * curMax
            curMax = max(i * curMax, i * curMin, i)
            curMin = min(i * curMin, tmp, i)
            res = max(res, curMax)
        return res
