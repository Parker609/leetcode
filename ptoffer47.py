"""
剑指 Offer 47. 礼物的最大价值
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、
直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
"""

"""
说实话，这个题我第一个反应竟然是深度优先遍历方法，但是看了看解析，发现这个题其实就是比较容易的动态规划方法，理由如下：
因为走路的方式只有向右和向下，所以最右下角的价值只能等于它的价值加上max（左侧的价值，上侧的价值），这样就比较容易想出来了吧。
"""
# 就不用numpy了，直接写。
def maxValue(grid):
  dp = [[0]*len(grid[0]) for _ in grid]
  dp[0][0] = grid[0][0]
  for row in range(len(grid)):
    for column in range(len(grid[0])):
      if row == 0 and column == 0:
        continue
      elif row == 0:
        dp[row][column] = dp[row][column - 1] + grid[row][column]
      elif column == 0:
        dp[row][column] = dp[row - 1][column] + grid[row][column]
      else:
        dp[row][column] = max(dp[row - 1][column], dp[row][column - 1]) + grid[row][column]
  return dp



if __name__ == '__main__':
  numGrid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
  ]
  res = maxValue(numGrid)
  print(res)