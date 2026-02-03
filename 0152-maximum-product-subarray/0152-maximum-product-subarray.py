class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMax, currMin = 1, 1
        for n in nums:
            temp = n * currMax
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(n * currMin, temp, n)
            res = max(currMax, res)
        return res