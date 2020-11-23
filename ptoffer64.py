"""
剑指 Offer 64. 求1+2+…+n
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
"""

# 其实就是简单的高斯求和，但是这边做出了诸多限制，所以才让这个题这么难。我的首选肯定是递归，但是递归的结束必须用条件语句，这边直接用逻辑运算的短路效应来搞定应该也可以。
def sumNums(n):
  return n>=1 and n+sumNums(n-1) or n

def sumNums2(n):
  if n ==1:
    return 1
  return sumNums2(n-1) +n

if __name__ == '__main__':
    res = sumNums(100)
    print(res)