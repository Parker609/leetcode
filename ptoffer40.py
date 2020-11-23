"""
剑指 Offer 40. 最小的k个数
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
"""

# 解题思路，其实就是数组的排列问题，但是只要最小的几个数，那么其实可以不用全排整个数组，当然如果想的话也可以对数组进行全排。

def getLeastNumbers(arr, k):
  resList = []
  def findSmallest(arr):
    smallestIndex = 0
    for i in range(len(arr)):
      if arr[i]<arr[smallestIndex]:
        smallestIndex = i
    return smallestIndex
  for i in range(k):
    smallestIndex = findSmallest(arr)
    resList.append(arr.pop(smallestIndex))
  return resList

if __name__ == '__main__':
    res = getLeastNumbers(arr = [0,1,2,1], k = 2)
    print(res)