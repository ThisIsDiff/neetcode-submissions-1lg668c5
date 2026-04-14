class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1, r = *max_element(piles.begin(), piles.end());
        int res = r;

        while (l<=r) {
            int mid = l + (r - l)/2;
            int hours = 0;

            for (auto& pile: piles) {
                hours += ceil((double) pile/mid);
            }

            if (hours > h) {
                l = mid + 1;
            } else {
                res = mid;
                r = mid - 1;
            }
        }
        return res;
    }
};
