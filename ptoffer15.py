"""
剑指offer第15题，二进制中1的个数。
请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。例如，把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 其实碰到类似的这种题的时候，碰到二进制的问题的时候，要多考虑二进制运算符法则，即与运算和或运算，还有平移运算之类的。
# 方法一，直接数位数。
def hammingWeight(n):
  # 这边有一个小技巧，1在二进制中的使用，是比较巧妙的。1和任何数做与运算，如果该数的二进制的最后一位是1，则返回1，否则返回0。
  counter = 0
  while n > 0:
    if n&1 == 1:
      counter += 1
    # 意思是将二进制向右移动一位。
    n >>= 1
  return counter

# 方法二，一个巧妙的方法，利用n&(n-1)，这个表达式可以让返回n的二进制表达式最右边的1变成0，这样可以直接数1的个数。
def hammingWeight2(n):
  counter = 0
  while n!= 0:
    n = n & (n - 1)
    counter += 1
  return counter

if __name__ == '__main__':
    res = hammingWeight2(9)
    print(res)