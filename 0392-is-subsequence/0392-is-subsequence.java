class Solution {
    public boolean isSubsequence(String s, String t) {
        int sLen = s.length(), sPos = 0;
        int tLen = t.length(), tPos = 0;
 
        // iterate s and t Read first char of s, compare with t
        // if first char found from s found, move sPos and tPos by 1 char
        // else move tPos by 1

        while (sPos<sLen && tPos<tLen){
            char sChar = s.charAt(sPos);
            char tChar = t.charAt(tPos);  
            
             if (sChar==tChar){
                sPos++;
                tPos++;
             }else{
                tPos++;
             }   
        }
        
        if(sPos==sLen && tPos<=tLen)
            return true;
        else
            return false;
    }
}