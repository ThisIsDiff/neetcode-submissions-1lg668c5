class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] res = new int[temperatures.length];
        Stack<int[]> st = new Stack<>();

        for (int i=0; i<temperatures.length; i++) {
            int temperature = temperatures[i];
            while (!st.isEmpty() && st.peek()[0] < temperature) {
                int[] temp = st.pop();
                res[temp[1]] = i - temp[1];
            }
            st.push(new int[]{temperature,i});
        }
        return res;
    }
}
