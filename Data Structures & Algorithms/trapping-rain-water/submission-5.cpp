class Solution {
public:
    int trap(vector<int>& height) {
        int waterArea = 0;
        int l = 0, r = height.size() -1;
        int leftmax = height[l], rightmax = height[r];

        while (l < r) {
            if (leftmax > rightmax) {
                r--;
                rightmax = max(rightmax, height[r]);
                waterArea += (rightmax - height[r]);
            } else {
                l++;
                leftmax = max(leftmax, height[l]);
                waterArea += (leftmax - height[l]);
            }
        }
        return waterArea;
    }
};
