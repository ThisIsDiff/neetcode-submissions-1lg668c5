class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0, r = heights.size() -1;
        int maxi = 0;
        while (l < r) {
            int area = min(heights[l], heights[r]) * (r-l);
            maxi = max(maxi, area);
            if (heights[l]>heights[r]) {
                r--;
            } else {
                l++;
            }
        }
        return maxi;
    }
};
