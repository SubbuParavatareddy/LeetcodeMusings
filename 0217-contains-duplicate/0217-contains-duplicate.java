class Solution {
    public boolean containsDuplicate(int[] nums) {
        boolean visited[] = new boolean[nums.length];
        Arrays.sort(nums);

        for (int i = 0; i < nums.length-1; i++) {
            if(nums[i]==nums[i+1])
                return true;
        }
        return false; 
    }
}