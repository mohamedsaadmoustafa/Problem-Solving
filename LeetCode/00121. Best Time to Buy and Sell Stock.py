class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy, max_profit =  prices[0], 0

        for current_price in prices:
            new_profit = current_price-buy

            if buy > current_price: 
                buy = current_price

            elif new_profit > max_profit:
                max_profit = new_profit

        return max_profit
