class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for idx, num in enumerate(nums):
            check_val = target - num
            if check_val in my_map:
                return idx, my_map[check_val]
            else:
                my_map[num] = idx
        return {}