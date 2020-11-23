"""
剑指 Offer 60. n个骰子的点数
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。

你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。
"""
"""
来个最简单的动态规划法吧,然后为了方便,让骰子的点数为0~5,这样和的最小的一端就不用更改了.
"""


def twoSum(n: int) -> list:
  """
  f(n,s)表示投n个筛子,点数和为s的概率,f(n+1,s) = f(n,s) * 1/6 + f(n,s-1) * 1/6+f(n,s-2) * 1/6+f(n,s-3) * 1/6+f(n,s-4) * 1/6+f(n,s-5) * 1/6
  n个色子可能出现的点数为从0~5n,那么可以按照这个规律做dp矩阵.
  :param n:
  :return:
  """
  dp = [[0]*(5*n+1) for i in range(n)]
  for i in range(0,6):
    dp[0][i] = 1/6
  for j in range(1,n):
    for k in range(5*(j+1)+1):
      dp[j][k] = (dp[j-1][k] + dp[j-1][k-1]+dp[j-1][k-2]+dp[j-1][k-3]+dp[j-1][k-4]+dp[j-1][k-5])*1/6
  print(dp)
  return dp[-1]

if __name__ == '__main__':
    res = twoSum(2)
    print(res)