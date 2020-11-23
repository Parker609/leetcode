"""
剑指 Offer 62. 圆圈中最后剩下的数字
0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。
"""

"""
解题思路,其实这个题就是传说中的约瑟夫环,首先提出暴力破解的方法,我们构建一个Node节点,来试试.
"""
class People():
  def __init__(self,x):
    self.value = x
    self.next = None

def lastRemaining( n: int, m: int) -> int:
  startPoint = People(0)
  a = startPoint
  for i in range(1,n):
    a.next = People(i)
    if a.next:
      a = a.next
  a.next = startPoint
  while startPoint.next != startPoint:
    counter = 0
    while counter < m-1:
      counter += 1
      if counter <m-1:
        startPoint = startPoint.next
    startPoint.next = startPoint.next.next
    startPoint = startPoint.next
  return startPoint.value

def lastRemaining2( n: int, m: int) -> int:
  """
  以上的方法当然可以解决这个问题,但是并不简洁,是使用了暴力破解的方法,那么是否有一个简单的算法可以解决这个问题呢,答案是有的.
  是使用倒推的方法,进行数学归纳.
  剩1人时,安全位置是0,即0位置不会被pass掉.
  剩2人时,安全位置是(0+m)%2
  剩3人时,安全位置是((0+m)%2+m)%3
  ... ...
  剩n人时,安全位置时(f(n-1)+m)%n
  """
  dp = [0] * (n+1)
  dp[1] = 0
  for i in range(2,n+1):
    dp[i] = (dp[i-1]+m)%i
  return dp[-1]





if __name__ == '__main__':
    res = lastRemaining2(10,17)
    print(res)