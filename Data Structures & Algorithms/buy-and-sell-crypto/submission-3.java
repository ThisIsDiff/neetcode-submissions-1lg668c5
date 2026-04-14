class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length < 2) return 0;

        int buylow = prices[0];
        int maxprofit = 0;
        for (int price: prices) {
            if (price > buylow) {
                int profit = price - buylow;
                maxprofit = Math.max(maxprofit, profit);
            } else {
                buylow = price;
            }
        }
        return maxprofit;
    }
}
