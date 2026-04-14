class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # fast = 1
        # slow = 0
        # size = len(nums)
        # while (nums[slow] != nums[fast]):
        #     slow = (slow + 1)%size
        #     fast = (fast + 2 )%size
        #     if slow == fast:
        #         fast = (fast + 1) %size
    
        # return nums[slow]

        slow = nums[0]
        fast = slow

        while (True):
            slow = nums[slow] #using numbers in the list as index/pointer since it could never go out of bound
            fast = nums[nums[fast]]

            if (slow == fast):
                break

        fast = nums[0]

        while (slow != fast):
            fast = nums[fast]
            slow = nums[slow]

        return slow