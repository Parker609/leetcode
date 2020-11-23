"""
剑指offer第16题，数值的整数次方。
实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 首先能想到的，就是把x乘自己n-1次
def myPow(x: float, n: int) -> float:
  for i in range(n-1):
    x *= x
  return x

# 所有迭代都是递归，所以可以用递归来实现，并且下方使用了一个小窍门，当一个数的偶数次次方的时候，比方说2的4次方，完全可以考虑为4的平方，减少迭代次数。
def myPow2(x,n):
  if n < 0:
    return myPow2(1/x,-n)
  if n == 0:
    return 1
  if n == 1:
    return x
  if n >1:
    if n % 2 == 0:
      return myPow2(x*x,n/2)
    else:
      return x * myPow2(x*x,(n-1)/2)

# 当然，基本上所有的题都会有一些莫名其妙的，不为人知的想法，利用幂的二进制来思考，但是结果好像和2的方法类似，只不过这边用的不是递归，而是迭代。
"""
比方说，n=18的情况下，假定x=2
那么18用2进制表示是10010
那么 18次 可以表示为 2**4 * 2**1 没办法贴图，就大概意思明白就行，所以先做n的分解。
"""
def myPow3(x,n):
  # 二进制其实就是对一个数取余数，然后反过来就行。
  if n < 0:
    x = 1/x
    n = -n
  res = 1
  # 下边的这个while其实写的很巧妙，算是简化之后的版本，其实原版如果根据二进制分解来说的话，其实还比较复杂的。
  while n!= 0:
    if n%2 == 1:
      res *= x
    x*=x
    # 将二进制左移一位。
    n//=2
  return res

if __name__ == '__main__':
    res = myPow4(2,0)
    print(res)