class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] A = nums1, B = nums2;

        if (nums1.length > nums2.length) {
            A = nums2;
            B = nums1;
        }

        int totalsize = nums1.length + nums2.length;
        int half = totalsize/2;
        int left = 0, right = A.length;
        while (true) {
            int x = left + (right - left)/2;
            int y = half - x ;

            int Aleft = x>0 ? A[x-1] : Integer.MIN_VALUE;
            int Aright = (x) < A.length ? A[x] : Integer.MAX_VALUE;
            int Bleft = y>0 ? B[y-1] : Integer.MIN_VALUE;
            int Bright = (y) < B.length ? B[y] : Integer.MAX_VALUE; 

            if ((Aleft<=Bright) && (Bleft<=Aright)) {
                if (totalsize%2 == 1) {
                    return ((double) Math.min(Aright,Bright));
                } else {
                    return ((double) (Math.max(Aleft,Bleft) + Math.min(Aright,Bright))/2.0);
                }
            } else if (Aleft > Bright) {
                right = x - 1;
            } else {
                left = x + 1;
            }
        }
    }
}
