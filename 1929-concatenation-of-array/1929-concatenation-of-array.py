class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n_len = len(nums)
        ans = [0] * (n_len * 2)
        for idx, num in enumerate(nums):
            ans[idx] = ans[idx + n_len] = nums[idx]
        return ans