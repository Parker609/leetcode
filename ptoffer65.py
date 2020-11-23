"""
剑指 Offer 65. 不用加减乘除做加法
写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。
"""


def add1(a, b):
  return sum(a, b)
  # 哈哈哈哈，只是用来搞笑的。


def add(a, b):
  """
  计算过程不让用最简单的加减乘除，那么就只能用位运算了，位运算其实并不简单。
  :param a:
  :param b:
  :return:
  """
  x = 0xffffffff
  a = a&x
  b = b&x
  # 这个地方分为加和位和进位计算，加和位直接做异或运算，进位是当前位的与运算。
  while b != 0:
    a, b = (a ^ b), (a & b) << 1 & x
  return a

if __name__ == '__main__':
  res = add(1, 3)
  print(res)