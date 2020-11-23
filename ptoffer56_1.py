"""
剑指 Offer 56 - I. 数组中数字出现的次数
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
"""

"""
还是用hash字典来做，因为已经知道最多出现两次，所以出现第一次添加，出现第二次删除，这样走一遍就能找到单独的数了，其实并不难。
"""
def singleNumbers(nums):
  tempList = []
  for i in nums:
    if i not in tempList:
      tempList.append(i)
    else:
      tempList.remove(i)
  return tempList

"""
通过解析，不得不说还是人才多啊，数学计算上少不了位运算，还是挺厉害的。
首先修改一下问题，如果这个数组中只有一个数出现了一次，剩下的数都是出现了两次，那么该怎么办，答：对整个数组所有数做异或运算，python中这个符号是^。
"""
def singleNumbers1(nums):
  """
  介绍一下异或运算的窍门，自己和自己 == 0，自己和0亦或 == 自己
  :param nums:
  :return:
  """
  tempNum =0
  for num in nums:
    tempNum ^= num
  return tempNum

"""
那么，当有两个出现了一次的数怎么办，那么就直接分组就可以了，分组按照二进制最终结果==1的那位分，因为相同的数这一位相同则必然分到一个组，而不同的则会分到不同的组，那么两个数必然被分开。
"""
def singleNumbers2(nums):
  """
  介绍一下异或运算的窍门，自己和自己 == 0，自己和0亦或 == 自己
  :param nums:
  :return:
  """
  tempNum =0
  for num in nums:
    tempNum ^= num
  d = 1
  while d & tempNum == 0:
    d <<=1
  a,b = 0,0
  for num in nums:
    if d&num:
      a^=num
    else:
      b^=num
  return a,b



if __name__ == '__main__':
    res = singleNumbers2([4,1,4,5,5,6,6,1,9,7])
    print(res)