"""
剑指 Offer 57 - II. 和为s的连续正数序列
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
"""

"""
还是使用双指针，左右指针中间的数列和等于target。
题目要求，序列里边至少含有两个数，所以比方说target=9，那么这个数列最多到5，否则5+6最少就是11，由此可以定数列范围。
然后用不同大小的窗口从左到右滑动，最小窗口大小为2，最大为整个序列，不过当sum()>target时，退出循环迭代。
这个题竟然是简单难度，莫非是因为有暴力破解的方法所以才是简单难度吗。
"""

def findContinuousSequence(target: int) -> list:
  sequence = [i for i in range(1,target//2+2)]
  windowLength = 1
  resList = []
  while sum(sequence[:windowLength])<target:
    for _ in range(len(sequence)-windowLength):
      # if sum(sequence[_:_+windowLength+1])==target:resList.append(sequence[_:_+windowLength+1])
      if (_+1+windowLength+1+_)*(windowLength+1)/2==target:resList.append(sequence[_:_+windowLength+1])
    windowLength += 1
  return sorted(resList,key=lambda x:x[0])

"""
上边的方法是肯定能跑出来的，但是这个方法更接近于暴力破解，在复杂度上并不占优势，所以还得说网上的大神是真的大神，共提出三种犯法，分别是：
滑动窗口->枚举求根法->间隔法，这三个方法，后两个方法都关系到数学计算，所以说编程编到最后会发现其实还是数学。就好像物理学到最后还是数学，物理学家数学都好。。。
"""
def findContinuousSequence2(target: int) -> list:
  sequence = [i for i in range(1, target // 2 + 2)]
  prePoint = 0
  sufPoint = 1
  resList = []
  while sufPoint < len(sequence):
    if (prePoint + sufPoint +2)*(sufPoint-prePoint+1)/2<target:
      sufPoint +=1
    elif (prePoint + sufPoint +2)*(sufPoint-prePoint +1)/2>target:
      prePoint += 1
    else:
      resList.append(sequence[prePoint:sufPoint+1])
      prePoint += 1
  return resList

def findContinuousSequence3(target: int) -> list:
  """
  但是上边的那个方法也并不是最好的方法，当然从逻辑上来讲其实是没问题的，这边要引入数学计算这个骚操作了，数学。。。呵呵哒。
  假定最终圈定的数列的首项是x，窗口长度是l，target简写为t，那么最终x=t/l + 1/2 - l/2,这个数应该是大于0的整数，在t已经给定的情况下遍历l可能的取值范围就可以得到x，
  再根据给定的l的值，就可以圈定这个数列了，代码如下：
  （l应该从2开始，长度可以通过等差数列求和公式得到，最大不能大于（2target）**0.5这么长）
  """
  resList = []
  sequence = [i for i in range(1, target // 2 + 2)]
  l = 2
  while l*l<2*target:
    if (target/l+0.5-0.5*l)>0 and (target/l+0.5-0.5*l)//1 == target/l+0.5-0.5*l:
      resList.append(sequence[int(target/l+0.5-0.5*l)-1:int(target/l+0.5-0.5*l)+l-1])
    l+=1
  return sorted(resList,key=lambda x:x[0])


if __name__ == '__main__':
    res = findContinuousSequence3(9)
    print(res)