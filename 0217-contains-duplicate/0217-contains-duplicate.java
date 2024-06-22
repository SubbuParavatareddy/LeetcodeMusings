import java.util.Hashtable;
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Hashtable<Integer, Integer> hTable = 
        new Hashtable<>();
        for (int i:nums){
            if(hTable.containsKey(i))
                return true;
            hTable.put(i, 1);
        }
        return false;
    }
}