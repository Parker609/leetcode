"""
剑指 Offer 63. 股票的最大利润
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
"""

"""
解题思路大体上是动态规划法,令f(n)表示前n天买卖一次股票所能得到的利润,那么:f(n+1)=max(f(n),n-min(list[:n]),简单粗暴.
"""
def maxProfit(prices: list) -> int:
  if len(prices)<2:
    return 0
  dp = [0] * (1+len(prices))
  dp[2] = prices[1] - prices[0]
  for i in range(3,len(prices)+1):
    dp[i] = max(dp[i-1],prices[i-1]-min(prices[:i]))
  if dp[-1] < 0:
    return 0
  else:
    return dp[-1]

if __name__ == '__main__':
    res = maxProfit([7,1,5,3,6,4])
    print(res)