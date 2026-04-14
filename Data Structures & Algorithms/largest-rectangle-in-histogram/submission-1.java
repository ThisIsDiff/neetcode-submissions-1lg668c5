class Solution {
    public int largestRectangleArea(int[] heights) {
        Stack<int[]> st = new Stack<>();
        int res = -1;

        for (int i=0; i<heights.length; i++) {
            int left = i;
            while (!st.isEmpty() && st.peek()[1] > heights[i]) {
                int[] indexHeight = st.pop();
                res = Math.max(res, indexHeight[1] * (i - indexHeight[0]));
                left = indexHeight[0];
            }
            st.push(new int[] {left,heights[i]});
        }

        for (int[] h : st) {
            res = Math.max(res, h[1] * (heights.length - h[0]));
        }
        return res;
    }
}
