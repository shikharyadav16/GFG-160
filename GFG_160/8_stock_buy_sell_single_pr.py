def maxProfit(prices, n):
    res = 0
    minimum = prices[0]
    
    for i in range(1, n):
        if (minimum < prices[i]):
            res = max(prices[i]-minimum, res)
        else:
            minimum = prices[i]
            
    return res
            
    
n = int(input("Enter the number of elements: "))
prices = []
for i in range(n):
    prices.append(int(input()))
    
print("Maximum profit is:", maxProfit(prices, n))
