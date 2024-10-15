
def maxProfit3(prices):


    l = 0
    r = 1
    maxP = 0
    minSoFar = prices[0]


    while r < len(prices):
        if prices[l] < prices[r]:
            minSoFar = min(minSoFar, prices[l])
            maxP = max(maxP, prices[r] - minSoFar)
        l += 1
        r += 1

    return maxP



prices = [7,6,4,3,1]
res = maxProfit3(prices)
print(res)






# def maxProfit(prices: list[int]) -> int:

#     maxProfit = float("-infinity") 
#     for i in range(len(prices) - 1):

#         j = i + 1
#         while j < len(prices):
#             maxProfit = max(maxProfit, prices[j] - prices[i])
#             j += 1
#     return maxProfit  if maxProfit > 0 else 0      
    






# prices = [7,1,5,3,6,4]
# res = maxProfit(prices)
# print(res)



# def maxProfit2(prices):

#     minFL = [prices[0]]
#     maxFR = [prices[-1]]
#     for i in range(1,len(prices)):
#         minFL.append(min(minFL[-1], prices[i]))
#         fromRight = len(prices) - i - 1
#         maxFR =  [max(maxFR[-1], prices[fromRight])] + maxFR

#     maxProfit = maxFR[0] - minFL[0]

#     for i in range(len(prices)-1):
#         maxProfit = max(maxProfit, maxFR[i] - minFL[i])
    
    
    
#     print(minFL)
#     print(maxFR)
#     return max(maxProfit,0)



# prices = [7,6,4,3,1]
# res = maxProfit2(prices)
# print(res)

