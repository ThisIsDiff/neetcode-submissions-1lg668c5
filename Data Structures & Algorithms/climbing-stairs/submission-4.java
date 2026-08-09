class Solution {
    public int climbStairs(int n) {
        int s1 = 1;
        int s2 = 2;

        if (n < 3) {
            return n;
        }

        for (int x = 2; x < n; x++) {
            int tmp = s1 + s2;
            s1 = s2;
            s2 = tmp;
        }
        return s2;
    }
}
