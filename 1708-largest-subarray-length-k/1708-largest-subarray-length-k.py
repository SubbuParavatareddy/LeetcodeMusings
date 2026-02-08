class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        max_elem_idx = 0

        for i in range(1, len(nums) - (k-1) ):

            if (nums[i] > nums[max_elem_idx] ):
                max_elem_idx = i
        
        return nums[max_elem_idx : max_elem_idx + k]