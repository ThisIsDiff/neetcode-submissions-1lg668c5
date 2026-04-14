class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
 
        l = 0
        r = 1
        res = 0
        while (r < len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                res = max(res, profit)
            else:
                l = r
            r += 1
        return res


"""
Input: prices = [10,1,5,6,7,1]

Output: 6

l = 0
r = 1
res = 6
min(l)= 10
max(r) = 1

to-do
- if l index is on index r, r increments 
- l or r keeps indexing depends on which has more profit, else would be indexing r
"""