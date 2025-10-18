class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr_len = len(nums)
        newarr = [0] * arr_len
        begin = 0
        end = arr_len-1
        pos = end
        while begin <= end:
            if abs(nums[begin]) < abs(nums[end]):
                newarr[pos] = nums[end] * nums[end]
                end-=1
                pos-=1
            else:
                newarr[pos] = nums[begin] * nums[begin]
                begin+=1
                pos-=1

        return newarr
