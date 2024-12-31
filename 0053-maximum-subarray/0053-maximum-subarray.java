class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum = nums[0];
        int currMax = nums[0];

        for (int i=1; i<nums.length; i++){
            if (currMax<0)
                currMax = 0;
            currMax = nums[i] + currMax;
            maxSum = Math.max(currMax, maxSum);
        }

        return maxSum;
    }
}