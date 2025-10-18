class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        const = increasing = decreasing = False
      
        nums_len = len(nums)
        if nums[0] == nums[nums_len-1]:
            const = True
        elif nums[0] < nums[nums_len-1]:
            increasing = True
        else:
            decreasing = True

        for i in range(len(nums) - 1):
            if const and nums[i] != nums[i + 1]:
                const = False
            if increasing and nums[i] > nums[i + 1]:
                increasing = False
            if decreasing and nums[i] < nums[i+1]:
                decreasing = False
      
        return const or increasing or decreasing