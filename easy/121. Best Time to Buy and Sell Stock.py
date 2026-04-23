# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                res = max(res, prices[r] - prices[l])
            else:
                l = r
            r += 1

        return res
        
# prices = [10,1,5,6,7,1] # 6
# prices = [10,8,7,5,2]   # 0
# prices=[3,2,6,5,0,3] # 4
prices=[7,1,5,3,6,4] # 5
print(Solution().maxProfit(prices))