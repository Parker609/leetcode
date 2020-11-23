"""
剑指offer第17题，打印从1到最大的n位数。
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。
"""

# 首先最能想到的是，需要一个循环。
def printNumbers(n):
  """
  简单来说，就是打印1到10的n次方再减一这么多数就可以了。
  :param n:
  :return:
  """
  res = []
  for i in range(1,10**n):
    res.append(i)
  return res

def printNumbers2(n):
  """
  这边竟然给了一个大数解法，就莫名其妙徒增难度。
  其实这个题如果不考虑大数的问题，其实挺好办，但是如果考虑大数的话，就不能这么简单的来做了，会超出数字的范围，所以如果考虑大数的话，其实还是使用str类型来做。
  这个题其实可以认定是0~9这10个数的n位全排列，全排列可以用递归来做。
  :param n:
  :return:
  """
  num = ['0'] * n
  res = []
  def dfs(x):
    if x == n:
      res.append(int("".join(num)))
      """
      '001'是字符串类型，直接用int转换一下就可以去掉前边的0，变成1。
      """
      return
    for i in range(10):
      num[x] = str(i)
      dfs(x+1)
  dfs(0)
  res.pop(0)
  return res




if __name__ == '__main__':
    res = printNumbers2(3)
    print(res)