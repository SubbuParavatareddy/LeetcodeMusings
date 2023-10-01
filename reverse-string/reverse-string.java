class Solution {
    public void reverseString(char[] s) {
        int bPt = 0, ePt = s.length-1;
        char bCh = Character.MIN_VALUE, tCh = Character.MIN_VALUE;
        while (bPt < ePt){
            
            tCh = s[bPt];
            s[bPt] = s[ePt];
            s[ePt] = tCh;
            
            bPt++;
            ePt--;
        }
    }
}