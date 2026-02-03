class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)
        currMax, currMin = 0, 0
        for n in nums:
            temp = n + currMax
            currMax = max(n + currMax, n + currMin, n)
            currMin = min(n + currMin, temp, n)
            res = max(currMax, res)
        return res