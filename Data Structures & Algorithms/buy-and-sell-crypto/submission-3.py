class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0 
        r = 1   
        if len(prices) ==1:
            return 0  
        max = prices[r]-prices[l]
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                
            if max < prices[r]-prices[l]:
                max = prices[r]-prices[l]

            r+=1    
            print(f"max:{max}")
          
        return max