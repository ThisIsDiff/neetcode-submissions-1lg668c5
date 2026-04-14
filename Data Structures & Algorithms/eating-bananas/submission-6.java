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
                // res = Math.min(res, mid);
                res = mid; // the reason why this works is because every time this else condition is met, it means that it is a valid answer and also lowers the right bound, such that everytime this else condition the mid get smaller compared to previous iterates, meaing Math.min(res,mid) is extra and unesscary.
                r = mid - 1;
            }
        }
        return res;
    }
}
