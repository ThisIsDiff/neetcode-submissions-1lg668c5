class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> st = new Stack<>();
        for (String t: tokens) {
            int temp;
            if (t.equals("+")) {
                int b = st.pop();
                int a = st.pop();
                temp = a + b;
            } else if (t.equals("-")) {
                int b = st.pop();
                int a = st.pop();
                temp = a - b;
            } else if (t.equals("*")) {
                int b = st.pop();
                int a = st.pop();
                temp = a * b;
            } else if (t.equals("/")) {
                int b = st.pop();
                int a = st.pop();
                temp = a / b;
            } else {
                temp = Integer.valueOf(t);
            }
            st.push(temp);
        }
        return st.pop();
    }
}
