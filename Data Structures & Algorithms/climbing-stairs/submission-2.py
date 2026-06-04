class Solution:
    def climbStairs(self, n: int) -> int:
        first_prev = 2
        second_prev = 3

        if n <= 3:
            return n

        steps = 3
        while steps < n:
            steps += 1

            nexts = first_prev + second_prev

            first_prev = second_prev
            second_prev = nexts

        return second_prev