class Solution:
    def climbStairs(self, n: int) -> int:
        first_prev = 1
        second_prev = 1



        steps = 1
        while steps < n:
            steps += 1

            nexts = first_prev + second_prev

            first_prev = second_prev
            second_prev = nexts

        return second_prev