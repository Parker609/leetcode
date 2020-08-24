"""
又到了开始各种找工作的日子了，面对各种笔试还是很难受的，作为一个程序员，要保持畅通的思路，所以每天刷刷算法题也挺好的，于是乎就瞄准了leetcode这个网站。
第一天需要恢复一下，不可能直接上来就做题，还是稍微补一补基础知识，今天的目标是算法课上的基础，排序算法和查找算法总结。
"""

"""
1.冒泡排序，是一种非常简单的排序方法，重复走过序列，对比相邻的数，将大的或者小的往后边放。时间复杂度为n2。
"""


def bubbleSort(numList):
  listLength = len(numList)
  for j in range(listLength):
    for i in range(listLength - j - 1):
      if numList[i] > numList[i + 1]:
        tempNum = numList[i]
        numList[i] = numList[i + 1]
        numList[i + 1] = tempNum
  print(numList)


"""
2.选择排序，在整个序列中寻找最大或者最小的数，然后和队首或队尾换位置，以此来排序数列。
"""


def selectionSort(numList):
  listLength = len(numList)
  for i in range(listLength):
    minNumIndex = i
    for j in range(i, listLength):
      if numList[j] < numList[minNumIndex]:
        minNumIndex = j
    numList[i], numList[minNumIndex] = numList[minNumIndex], numList[i]
  print(numList)


"""
3.插入排序，是一种简单直观算法，它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
"""


def insertionSort(numList):
  listLength = len(numList)
  for i in range(1, listLength):
    for j in range(i):
      if numList[i] < numList[j]:
        tempNum = numList.pop(i)
        numList.insert(j, tempNum)
        break
  print(numList)


"""
4.希尔排序，希尔排序是对插排的改进版，其实就是将整个数组分组进行插排，这样可以让时间复杂度减少到n2之下。
"""


def shellSort(numList):
  listLength = len(numList)
  # 这边的gap这样设定是有一定规则的，一般用数组长度的一半就可以，向下取整。
  gap = int(listLength / 2)
  while gap >= 1:
    for i in range(gap, listLength):
      for j in range(0, i, gap):
        if numList[i] < numList[j]:
          tempNum = numList.pop(i)
          numList.insert(j, tempNum)
          break
    gap = int(gap / 2)
  print(numList)


"""
5.归并排序，是一种有效的排序方法，是分而治之的典型应用，时间复杂度只有 nlogn 很稳定。+
  分而治之的思想，不过代码写起来是递归的样式。
"""


def mergeSort(numList):
  listLength = len(numList)
  if listLength < 2:
    return numList
  midPoint = int(listLength / 2)
  leftList = numList[:midPoint]
  rightList = numList[midPoint:]
  return merge(mergeSort(leftList), mergeSort(rightList))


def merge(leftList, rightList):
  resList = []
  while len(leftList) > 0 and len(rightList) > 0:
    if leftList[0] <= rightList[0]:
      resList.append(leftList.pop(0))
    else:
      resList.append(rightList.pop(0))
  while len(leftList) > 0:
    resList.extend(leftList)
    leftList = []
  while len(rightList) > 0:
    resList.extend(rightList)
    rightList = []
  return resList


"""
6.快速排序，简单来说，快速排序就是找到数列中所有数所应该属于的index值。
"""


def quickSort(numList):
  listLength = len(numList)
  if listLength < 2:
    return numList
  lowPoint = 0
  highPoint = listLength - 1
  tempNum = numList[lowPoint]
  while lowPoint != highPoint:
    while lowPoint != highPoint and numList[highPoint] > tempNum:
      highPoint -= 1
    numList[lowPoint] = numList[highPoint]
    while lowPoint != highPoint and numList[lowPoint] < tempNum:
      lowPoint += 1
    numList[highPoint] = numList[lowPoint]
  return quickSort(numList[:lowPoint]) + [tempNum] + quickSort(numList[lowPoint + 1:])


"""
7.堆排序，利用堆的性质来进行排序，大顶堆，小顶堆。
  构建堆的时候，有一个说明，在数组中，父节点的编号的二倍，是左子节点，二倍加一，是右子节点。
  此算法中，最难的地方就是堆调整。
"""


# 调整堆
def adjustHeap(arr, i):
  leftIndex = i * 2
  rightIndex = i * 2 + 1
  if rightIndex < len(arr) and arr[i] < arr[rightIndex]:
    arr[i], arr[rightIndex] = arr[rightIndex], arr[i]
  if arr[i] < arr[leftIndex]:
    arr[i], arr[leftIndex] = arr[leftIndex], arr[i]


def heapSort(numList):
  numList.insert(0, '#')
  tempList = []
  while len(numList) > 2:
    midIndex = int((len(numList) - 1) / 2)
    for i in range(midIndex):
      adjustHeap(numList, midIndex - i)
    numList[1], numList[-1] = numList[-1], numList[1]
    tempList.append(numList.pop())
  tempList.append(numList.pop())
  return tempList


if __name__ == '__main__':
  testNumList = [2, 6, 3, 9, 4, 5, 1, 0]
  res = heapSort(testNumList)
  print(res)
