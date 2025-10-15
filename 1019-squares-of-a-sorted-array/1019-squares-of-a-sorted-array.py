class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        newarr = []
        for num in nums:
            newarr.append(num*num)
        newarr.sort()
        return newarr        