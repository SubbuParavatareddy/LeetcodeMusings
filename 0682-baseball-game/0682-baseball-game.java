class Solution {
    public int calPoints(String[] operations) {
        int cap = operations.length;
        int tot = 0, len = 0, lenRes = 0, temp = 0;
        String[] res = new String[cap];
        for (int i = 0; i < cap; i++) {
            String val = operations[i];
            if (val.equals("C")) {
                res[lenRes-1] = "";
                lenRes--;
            } else if (val.equals("D")) {
                temp = Integer.valueOf(res[lenRes-1]) * 2;
                res[lenRes] = String.valueOf(temp);
                lenRes++;
            } else if (val.equals("+")) {
                temp = Integer.valueOf(res[lenRes - 1]) + Integer.valueOf(res[lenRes - 2]);
                res[lenRes] = String.valueOf(temp);
                lenRes++;
            } else {
                res[lenRes] = val;
                lenRes++;
            }
        }
        for (int i = 0; i < lenRes; i++) {
            System.out.println(res[i]);
            tot += Integer.valueOf(res[i]);
        }
        return tot;
    }
}