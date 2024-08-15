class Solution {
    public int longestOnes(int[] nums, int k) {
        int left = 0, right = 0, ans = 0, curr = 0;
        for (right=0; right<nums.length; right++){
            if (nums[right]==0)
                curr++;
            while (curr > k){
                if (nums[left]==0){
                    curr--;
                }
                left++;
            }
            ans = Math.max(ans, right-left+1);
        }
        return ans;
    }
}