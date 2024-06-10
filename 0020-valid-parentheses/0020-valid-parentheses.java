class Solution {
    public boolean isValid(String s) {
        HashMap<Character, Character> maps = new HashMap<>();
        maps.put(')','(');
        maps.put(']','[');
        maps.put('}','{');
        Stack<Character> stack = new Stack<>();
        for (char ch: s.toCharArray()){
            if (!maps.containsKey(ch)){
                stack.push(ch);
            }else{
                 if(stack.empty() || stack.pop() != maps.get(ch) )
                    return false;   
            }
        }
        return stack.empty();
    }
}