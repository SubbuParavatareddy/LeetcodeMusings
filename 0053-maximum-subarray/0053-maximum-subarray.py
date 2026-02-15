class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)
        cur_max, cur_min = 0, 0
        for num in nums:
            tmp = cur_max + num
            cur_max = max(cur_max + num, cur_min + num, num)
            cur_min = min(cur_min + num, tmp, num)
            res = max(cur_max, res)
        return res