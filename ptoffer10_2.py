"""
剑指 Offer 10-2. 青蛙跳台阶问题
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
"""
from functools import lru_cache


# 显然也是个递归，这个可以反着想，比方说上第n级台阶，其实就是上第n-1个台阶的方法种类再迈一步，其实就是n-1个台阶那么多种，或者n-2个台阶那么多种类再上一步。
# 递归的东西应该仔细思考一下，再简单也要思考一下，细思极恐。
@lru_cache()
def numWays(n):
  if n == 0:
    return 1
  elif n == 1:
    return 1
  elif n == 2:
    return 2
  else:
    return numWays(n - 1) + numWays(n - 2)
