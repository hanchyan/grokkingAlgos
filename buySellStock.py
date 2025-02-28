class Solution(object):
    def maxProfit(self, prices):
        returns = []
        for i in prices:
            for l in prices:
                p = (i-l)
                returns.append(p)
        print(returns)

            

solution = Solution()
result = solution.maxProfit([7,1,5,3,6,4])
print(result)
        
        
       



       
"""
so here i want to find the largest negative range between one thing and another (example
1-6 = -5, buy for 1 sell for 6 make 5... so i want to test each value minus each value and
then find the largest negative number)
"""
        
"""
:type prices: List[int]
:rtype: int
"""
        