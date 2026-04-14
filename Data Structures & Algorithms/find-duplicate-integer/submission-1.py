class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 1
        slow = 0
        size = len(nums)
        while (nums[slow] != nums[fast]):
            slow = (slow + 1)%size
            fast = (fast + 2 )%size
            if slow == fast:
                fast = (fast + 1) %size
    

        return nums[slow]