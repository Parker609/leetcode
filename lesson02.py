"""
在lesson01里边大改统计了目前已有的排序算法，既然排序算法大改整理完了，那么接下来就是查找算法。
即在数列中寻找目标值。
一半分为无序查找和有序查找，即被查找的数列是有序的还是无序的。
"""

"""
1.顺序查找，不要被这个名字骗了，它实际上是无序查找算法中的一种，从数据表的一端开始，顺序扫描，直到找到自己想要的值为止。
"""


def sequenceSearch(numList, targetNum):
  for i in range(len(numList)):
    if numList[i] == targetNum:
      return i + 1
  return False


"""
2.折半查找，时间复杂度为log2n，是有序查找的一种。
"""


def binarySearch(numList, targetNum):
  listLength = len(numList)
  low = 0
  high = listLength - 1
  mid = int(low + (high + low) / 2)
  while low < high:
    if numList[mid] < targetNum:
      low = mid
      mid = int(low + (high - low) / 2)
    elif numList[mid] == targetNum:
      return mid + 1
    else:
      high = mid
      mid = int(low + (high + low) / 2)
  return False


"""
3.插值查找，这种查找方式其实算是折半查找的改进版，比方说如果在字典中查Apple的话，绝对不会从中间开始查，而是会在开头查找，反过来如果查Zoo的话，也是从后边找，所以mid的定义就可以有操作了
"""


def insertSearch(numList, targetNum):
  listLength = len(numList)
  low = 0
  high = listLength - 1
  mid = int(low + (high - low) * (targetNum - numList[low]) / (numList[high] - numList[low]))
  while low < high:
    if numList[mid] < targetNum:
      low = mid
      mid = int(low + (high - low) * (targetNum - numList[low]) / (numList[high] - numList[low]))
    elif numList[mid] == targetNum:
      return mid + 1
    else:
      high = mid
      mid = int(low + (high - low) * (targetNum - numList[low]) / (numList[high] - numList[low]))
  return False


"""
4.斐波那契查找，也是二分查找的一种提升，也是在mid的取值上做文章，简单来说，就是用斐波那契数列来将整个数列分开。
  其中有一个取巧的地方，mid=low+F（k-1）-1
  解释一下为什么这么取值，由斐波那契数列可知，F(k)=F(k-1)+F(k-2),那F(k)-1=(F(k-1)-1)+(F(k-2)-1)+1,所以数组长度只要满足 F(k)-1，就可以将数组分为F(k-1)-1和F(k-2)-1左右两部分，其中mid=low+F(k-1)-1
"""


# 构建斐波那契数列的方法，迭代类型，k为数列下标。
def constructFib(k):
  if k < 2:
    return 1
  else:
    return constructFib(k - 2) + constructFib(k - 1)


def fibSearch(numList, targetNum):
  listLength = len(numList)
  low = 0
  high = listLength - 1
  k = 0
  while listLength > constructFib(k) - 1:
    k += 1
  mid = low + constructFib(k - 1) - 1
  while low < high:
    if targetNum == numList[mid]:
      return mid
    elif targetNum < numList[mid]:
      high = mid
      # k的值减小了1，那么目前的constructFib(k)-1就是左边部分的长度。
      k -= 1
    elif targetNum > numList[mid]:
      # k的值减小了2，那么目前的constructFib(k)-1就是右边部分的长度。
      low = mid
      k -= 2
    # 更新mid的值。
    mid = low + constructFib(k - 1) - 1
    # 其实这边或许会有一个疑问，那就是当k<3的时候，constructFib(k-1)的返回值为1，那么mid会一直===low，其实是不会有这种情况的，当mid===low之前，会有一个判断，这边自己想一下长度为2的数组发生的情况就可以了。
  return False


"""
5.树表查找，首先是最简单的树表查找，二叉树查找算法。
  基本思想，二叉查找树先对待查找的树进行生成树，确保树的左分支的值小于右分支的值，
"""


class TreeNode():
  def __init__(self, index, value, leftNode=None, rightNode=None):
    self.value = value
    self.index = index
    self.leftNode = leftNode
    self.rightNode = rightNode


def binaryTreeSearch(numList, targetNum):
  root = TreeNode(0, numList[0])
  point = root
  listLength = len(numList)
  for i in range(1,listLength - 1):
    if numList[i] < point.value:
      pass



if __name__ == '__main__':
  numList = [9, 4, 6, 8, 2, 1, 0, 3836]
  sortdeList = [1, 2]
  res = fibSearch(sortdeList, 1)
  print(res)
