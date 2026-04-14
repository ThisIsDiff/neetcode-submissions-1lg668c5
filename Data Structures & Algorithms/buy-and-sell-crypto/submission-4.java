class Solution {
    public int maxProfit(int[] prices) {
        // 2 pointers
        // if (prices.length < 2) return 0;

        // int buylow = prices[0];
        // int maxprofit = 0;
        // for (int price: prices) {
        //     if (price > buylow) {
        //         int profit = price - buylow;
        //         maxprofit = Math.max(maxprofit, profit);
        //     } else {
        //         buylow = price;
        //     }
        // }
        // return maxprofit;

        // dynamic programming
        
        int maxprofit = 0;
        int buylow = prices[0];
        for (int price: prices) {
            maxprofit = Math.max(maxprofit, price - buylow);
            buylow = Math.min(buylow, price);
        }
        return maxprofit;
        
    }
}
