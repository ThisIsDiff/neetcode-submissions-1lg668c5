class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_one = 0
        cost_two = cost[0]

        for i in range(1,len(cost)):
            tmp = cost_two 
            cost_two = cost[i] + min(cost_one,cost_two)
            cost_one = tmp

        return min(cost_one,cost_two)