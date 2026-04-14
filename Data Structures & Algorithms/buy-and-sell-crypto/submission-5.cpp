class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // 2 pointers 
        int buylow = prices[0];
        int maxprofit = 0;

        for (int& price: prices) {  // price act as the right pointer 
            if (price > buylow) {   // buylow act as the left pointer
                int profit = price - buylow;
                maxprofit = max(maxprofit, profit);
            } else {
                buylow = price;
            }
        }
        return maxprofit;
    }
};
