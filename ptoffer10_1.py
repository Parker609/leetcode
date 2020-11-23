"""
剑指offer第10-1题，斐波那契数列。
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。
注意：python中有一个 @lru_cache 装饰器，用在递归中，重复内存重复利用。
"""

from functools import lru_cache

@lru_cache()
def fib(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fib(n-1)+fib(n-2)

if __name__ == '__main__':
    # 递归就这么简单，其实也并不简单。
  res = fib(5)
  print(res)