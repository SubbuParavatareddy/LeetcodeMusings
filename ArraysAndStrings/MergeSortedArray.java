public class MergeSortedArray {
    public static void main(String[] args){
        int[] nums1 = merge(new int[]{1, 2, 3, 0, 0, 0}, 3, new int[]{2, 5, 6}, 3);
        for (int i=0; i<nums1.length; i++)
            System.out.println(nums1[i]);
    }
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = nums1.length - 1, j = nums2.length - 1;
        int idx = m + n - 1;
        while ( n > 0 ) {
            if (m>0 && nums1[m-1]>nums2[n-1]) {
                nums1[idx] = nums1[m-1];
                m--;
            }else{
                nums1[idx] = nums2[n-1];
                n--;
            }
            idx--;
        }
    }
}
