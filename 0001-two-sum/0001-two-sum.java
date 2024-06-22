import java.util.*;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] retArr = new int[2];
        LinkedHashMap<Integer, Integer> lHm = 
            new LinkedHashMap<>();
        int remaining = 0;
        for (int i=0; i<nums.length; i++){
            int val = nums[i];
            remaining = target - val;
            if(!lHm.containsValue(remaining))
                lHm.put(i, val);
            else{
                for (Map.Entry<Integer,Integer> entry : lHm.entrySet()) {
                       retArr[0]=i; 
                       if (entry.getValue()==remaining) {
                            retArr[1]=entry.getKey();
                            break;
                       }
                    }
            }
        }

        return retArr;
    }
}