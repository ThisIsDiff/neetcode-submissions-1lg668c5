class Solution {
    public int findDuplicate(int[] nums) {
        int slow = 0;
        int fast = 1;
        int size = nums.length;
        while (nums[slow] != nums[fast]) {
            slow = (slow + 1) % size;
            fast = (fast + 2) % size;

            if (slow == fast) {
                fast = (fast + 1) % size;
            }
        }
        return nums[slow];
    }
}
