class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = 0
        for i, num in enumerate(nums):
            if i < len(nums) - 1 and nums[i] == nums[i+1]:
                continue
            else:
                nums[res] = nums[i]
                res += 1
        return res