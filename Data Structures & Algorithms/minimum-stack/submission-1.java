class MinStack {

    private Stack<Integer> stack;
    private Stack<Integer> minval;
    public MinStack() {
        stack = new Stack<>();
        minval = new Stack<>();
    }
    
    public void push(int val) {
        stack.push(val);
        if (!minval.isEmpty() && minval.peek() < val) {
            val = minval.peek();
        }
        minval.push(val);
    }
    
    public void pop() {
        stack.pop();
        minval.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minval.peek();
    }
}
