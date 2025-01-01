class Solution {
    public int maxProduct(int[] nums) {
        int maxProduct = nums[0]; 
        int minProduct = nums[0];
        int answer = nums[0];
      
        // Iterate through the array starting from the second element.
        for (int i = 1; i < nums.length; ++i) {
            // Store the current max and min before updating them.
            int currentMax = maxProduct;
            int currentMin = minProduct;
          
            // Update the maxProduct to be the maximum between the current number, 
            // currentMax multiplied by the current number, and currentMin multiplied 
            // by the current number. This accounts for both positive and negative numbers.
            maxProduct = Math.max(nums[i], Math.max(currentMax * nums[i], currentMin * nums[i]));
          
            // Update the minProduct similarly by choosing the minimum value.
            minProduct = Math.min(nums[i], Math.min(currentMax * nums[i], currentMin * nums[i]));
          
            // Update the answer if the newly found maxProduct is greater than the previous answer.
            answer = Math.max(answer, maxProduct);
        }
      
        // Return the largest product of any subarray found.
        return answer;
    }
}