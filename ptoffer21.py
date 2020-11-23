"""
剑指 Offer 21. 调整数组顺序使奇数位于偶数前面

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
"""

# 基本思路，前后两个指针，当前边的指针碰到偶数，后边的指针碰到奇数二者呼唤，否则前指针加一后指针减一。。
def exchange(numList):
  listLen = len(numList)
  startIndex = 0
  finalIndex = listLen -1
  while startIndex < finalIndex:
    if numList[startIndex]/2 == numList[startIndex] // 2 and numList[finalIndex]/2 != numList[finalIndex]//2:
      numList[startIndex],numList[finalIndex] = numList[finalIndex],numList[startIndex]
    elif numList[startIndex]/2 != numList[startIndex] // 2:
      startIndex += 1
    elif numList[finalIndex]/2 == numList[finalIndex]//2:
      finalIndex -= 1
  return numList


# 代码优化如下
def exchange2(numList):
  startIndex = 0
  finalIndex = len(numList) -1
  while startIndex < finalIndex:
    # 判断数字基数还是偶数，可以用二进制的与运算来做。
    while numList[startIndex] & 1 == 1:
      startIndex += 1
    while numList[finalIndex] & 1 == 0:
      finalIndex -= 1
    numList[startIndex], numList[finalIndex] = numList[finalIndex], numList[startIndex]
  return numList
if __name__ == '__main__':
    res = exchange([1,2,3,4])
    print(res)