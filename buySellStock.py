class Solution(object):
    def maxProfit(self, prices):
        returns = []
        pairs = []
        pair = []
        for i in range(len(prices)):
            for l in prices[i+1:]:
                # print(prices[i])
                # print(l)
                pairs.append(prices[i])
                pairs.append(l)
                p = prices[i]-l
                returns.append(p)
        # for i in returns:
        #     if returns[i] > returns[i +1]:
        #         returns.pop(i)
            print(pairs)
            print(returns)

""""
the output is pretty good... for pairs i need to put each pair into its own list and then put that list into pairs so there is 
a one to one match for pair and each result of determing profit so i can pair the indexes 
""""

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
        