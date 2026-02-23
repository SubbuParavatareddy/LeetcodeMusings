class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n_len = len(nums)
        res = [0] * n_len * 2
        for i, val in enumerate(nums):
            res[i] = res[i+n_len] = val
        return res