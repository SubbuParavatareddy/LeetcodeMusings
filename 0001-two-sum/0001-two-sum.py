class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in nums_map:
                return [idx, nums_map[diff]]
            nums_map[val] = idx
        return []