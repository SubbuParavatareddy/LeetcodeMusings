public class ReverseString {
    public static void main(String[] args){
        char[] s = reverse("hello".toCharArray());
        System.out.println(s);
    }
    public static char[] reverse(char[] s) {
        int bPt = 0, ePt = s.length-1;
        char temp = Character.MIN_VALUE;
        while (bPt < ePt){
            
            temp = s[bPt];
            s[bPt++] = s[ePt];
            s[ePt--] = temp;
            
        }
        return s;
    }
}