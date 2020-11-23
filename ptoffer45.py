"""
剑指 Offer 45. 把数组排成最小的数
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
"""

"""
简单说一下解题思路，第一个反应就是将数组里所有的数都给拆成1位数，把所有的0都拿出来剩余的数从小到大排序，然后把所有的0在第2位插入。
但是这个方法有点想当然了，比方说[20,1]这个数组，我们会返回最小值102，但是这个最小应该是120，于是提出方法2。
"""

def minNumber(nums):
  tempList = sorted(list(map(int,list("".join(map(str,nums))))))
  tempIndex = 0
  while tempIndex < len(tempList):
    if tempList[tempIndex]!= 0:
      break
    tempIndex +=  1
  aList = tempList[tempIndex:]
  aList.insert(1,"".join(list(map(str,tempList[:tempIndex]))))
  res = "".join(list(map(str,aList)))
  return res

"""
思路2，其实就是数组里边所有数的排序问题，比方说30和34，如果3034<3430，那么，就把30排在34的前边，用这个规则来确定排序法则，对整个数组进行排序。
利用这个法则，嵌入到任意一种排序方法里就可以了，首先实现一个最简单的快排，再把这个方法嵌入进去。不过好像直接用sort来做也行，权当是复习快排了。
"""
def aSmallerb(a,b):
  if int(str(a)+str(b)) < int(str(b)+str(a)):
    return True
  else:
    return False


def minNumber2(nums):
  if len(nums) < 2:
    return nums
  startIndex = 0
  finalIndex = len(nums) -1
  tempNum = nums[0]
  while startIndex < finalIndex:
    while startIndex < finalIndex and aSmallerb(tempNum,nums[finalIndex]):
      finalIndex -= 1
    nums[startIndex] = nums[finalIndex]
    while startIndex < finalIndex and not aSmallerb(tempNum,nums[startIndex]):
      startIndex += 1
    nums[finalIndex] = nums[startIndex]
  return minNumber2(nums[:startIndex]) + [tempNum] + minNumber2(nums[startIndex+1:])

if __name__ == '__main__':
    res = minNumber2([13,4,5,2,1])
    print("".join(list(map(str,res))))
    print(res)