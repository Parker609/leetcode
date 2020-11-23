"""
剑指 Offer 43. 1～n 整数中 1 出现的次数
输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。

例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。
"""

def countDigitOne(n: int) -> int:
  """
  其实就是简单的找规律,感觉所有的计算机问题最终都会变成数学问题,都是逻辑的问题.
  某一位出现的1的次数,是和本身的大小有关系的.
  假定一个数是pre+cur+suf三部分构成的,比方说13924,cur=9,那么pre=13,suf=24,dig表示这是哪一位,十位还是百位这个意思.
  当cur为0的时候,这一位1出现的次数是由前面几位决定的,pre * dig.
  当cur为1的时候,这一位出现次数是由前面几位和后面几位一起决定的,pre*dig + suf +1,比方说是4,那么就10\11\12\13\14.
  当cur大于1的时候,这一位的出现次数由前几位决定,(pre+1)*dig
  从后往前捋,到头就能得出结果了.
  :param n:
  :return:
  """
  nStr = str(n)
  pointIndex = len(nStr)-1
  dig = 1
  res = 0
  while pointIndex >= 0:
    cur = int(nStr[pointIndex])
    pre = int(nStr[:pointIndex] or 0)
    suf = int(nStr[pointIndex+1:] or 0)
    if cur == 0:
      res += pre*dig
    elif cur ==1:
      res += (pre*dig + suf +1)
    else:
      res+= (pre+1)*dig
    dig *= 10
    pointIndex -= 1
  return res

if __name__ == '__main__':
  res = countDigitOne(12)
  print(res)