"""
剑指 Offer 11. 旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。
"""


# 这个问题有多种解题思路，比方说第一种：暴力破解，最简单的思路，只要找到一个后边比自己小，这个数就是最小值。
def findMin(numList):
  listLength = len(numList)
  for i in range(listLength - 1):
    if numList[i] > numList[i + 1]:
      return numList[i + 1]
  if numList[-1] >= numList[0]:
    return numList[0]

# 第二种解法，虽然是旋转数列，但是里边还是有顺序的。所以这边也可以使用二分法试一试。
def findMin2(numList):
  #关于旋转数列有一个特点，在数列中任意取两个数，只要右侧的比左侧的大，那么两个数中间的数列一定是正向递增的，所以在二分中可以使用这一特点。
  listLength = len(numList)
  left = 0
  right = listLength -1
  mid = int(0.5*(right - left))
  while left < right:
    if numList[right] > numList[mid]:
      right = mid
    elif numList[right] < numList[mid]:
      left = mid+1
    else:
      left += 1
    mid = left + int(0.5 * (right - left))
  return numList[mid]



if __name__ == '__main__':
  numList = [2, 2, 2, 0, 1]
  res = findMin2(numList)
  print(res)
