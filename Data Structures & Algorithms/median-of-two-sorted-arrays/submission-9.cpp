class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int>& A = nums1, B = nums2;
        if (A.size() > B.size()) {
            swap(A,B);
        }
        int totalsize = A.size() + B.size();
        int half = totalsize/2;
        int left = 0, right = A.size();

        while (true) {
            int mid = left + (right - left)/2;
            int y = half - mid;

            int Aleft = mid > 0 ? A[mid-1] : INT_MIN;
            int Aright = mid < A.size() ? A[mid] : INT_MAX;
            int Bleft = y > 0 ? B[y-1] : INT_MIN;
            int Bright = y < B.size() ? B[y] : INT_MAX;

            if ((Aleft <= Bright) && (Bleft <= Aright)) {
                if ((totalsize%2) == 1) {
                    return min(Aright, Bright);
                } else {
                    return ((max(Aleft,Bleft) + min(Aright, Bright)) / 2.0);
                }
            } else if (Aleft > Bright) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
    }
};
