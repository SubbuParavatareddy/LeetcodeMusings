class Solution {
    public int[] sortedSquares(int[] nums) {
        int len = nums.length;
        int res[] = new int[len];
        int left = 0, right = len-1, num=0;
        int i=right;
        //for (int i=right; i>=0; i--){
        while (left<=right){            
              if (Math.abs(nums[left]) < 
                    Math.abs(nums[right]) ){
                num = nums[right];
                right--;                  
              }else{
                num = nums[left];
                left++;
              }
            //res[i] = num * num;
            res[i--] = num * num;            
        }
        return res;
    }
}