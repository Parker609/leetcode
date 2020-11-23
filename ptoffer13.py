"""
剑指offer第13题，机器人的运动范围。
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到
方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，
因为3+5+3+8=19。请问该机器人能够到达多少个格子？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 简单考虑，其实还是属于矩阵搜索问题，可以用深度优先算法来解决，其实和8皇后问题差不多。
def sums(num):
  #  首先是数位相加的简单算法。
  s = 0
  while num != 0:
    s+=num%10
    num = num//10
  return s

# 直接用深度优先算法强行暴力破解，不过算法运行时间比较长，这也是没办法的事情，回头再来考虑时间复杂度小一点的。

visitPoint = []
def movingCount(x,y,k,m,n):
  if sums(x)+sums(y) > k or x<0 or x>=m or y <0 or y>= n or [x,y] in visitPoint:
    return 0
  else:
    visitPoint.append([x,y])
    return 1 + movingCount(x,y+1,k,m,n) + movingCount(x+1,y,k,m,n)


if __name__ == '__main__':
    res = movingCount(0,0,9,15,38)
    print(res)