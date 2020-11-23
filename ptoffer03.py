"""
Leetcode剑指offer第一题，之前明明做过了，但是是重新刷题嘛，再刷一遍。
找出数组中重复的数字。

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 这个题用哈希表方法解是最合适的，直接从头到尾走一遍整个数组即可。
def findRepeatNumber(numList):
  tempDict = {}
  resList = []
  for i in numList:
    if i not in tempDict:
      tempDict[i] = 1
    else:
      # 这边 return i 是说返回任意一个就可以，如果返回所有的话，可以返回一个列表。
      # return i
      resList.append(i)
  return resList



if __name__ == '__main__':
    numList = [2, 3, 1, 0, 2, 5, 3]
    res = findRepeatNumber(numList)
    print(res)