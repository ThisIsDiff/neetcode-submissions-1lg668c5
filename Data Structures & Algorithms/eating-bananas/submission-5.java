class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int l = 0, r = Arrays.stream(piles).max().getAsInt();
        int res = r;

        while (l<=r) {
            int mid = l + (r - l)/2;
            int hours = 0;
            for (int pile: piles) {
                hours += Math.ceil((double) pile/mid);
            }

            if (hours > h) {
                l = mid + 1;
            } else {
                res = Math.min(res, mid);
                r = mid - 1;
            }
        }
        return res;
    }
}
