class Solution {
    public int calPoints(String[] ops) {
        Deque<Integer> stack = new ArrayDeque<>();
        int tot = 0;

        for (String op: ops){
            if (op.equals("+")){
                int top = stack.pop();
                int newtop = top + stack.peek();
                stack.push(top);
                stack.push(newtop);
            }else if (op.equals("C")){
                stack.pop();
            }else if (op.equals("D")){
                stack.push(stack.peek()*2);
            }else{
                stack.push(Integer.valueOf(op));
            }
        }
        for(int score: stack) 
            tot+= score;
        return tot;
    }
}