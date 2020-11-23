"""
剑指 Offer 61. 扑克牌中的顺子
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。
"""

"""
解题思路，总共五个数，按照递增顺序排列，然后拿出来所有的0，做一个5位的动态规划，当dp全都为true的时候，则返回true。
"""


def isStraight(nums: list) -> bool:
  nums = sorted(nums)
  zeroIndex = 0
  zeroList = []
  while nums[zeroIndex] == 0:
    zeroList.append(0)
    nums.pop(0)
  tempNum = [0]*5
  tempNum[0] = nums.pop(0)
  for i in range(1,5):
    tempNum[i] = nums.pop(0) if len(nums)>0 and nums[0] - tempNum[i-1] == 1 else tempNum[i-1]+1+zeroList.pop() if len(zeroList)>0 else False
  for i in tempNum:
    if not i:
      return False
  return True

if __name__ == '__main__':
    res = isStraight([0,0,1,2,5])
    print(res)