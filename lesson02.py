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
  基本思想，二叉查找树先对待查找的树进行生成树，确保树的左分支的值小于父节点小于右分支的值，在查找之前，首先要针对已有数据构建二叉查找树。
  如果对查找二叉树进行中序排列的话，可以得到有序数列。
"""


# 创建二叉查找树（BST，Binary Search Tree)。

class BinarySearchTree():
  def __init__(self, value):
    self.value = value
    self.leftNode = None
    self.rightNode = None

  # 递归的方式，递归果然不容易理解。
  def insertNode(self, value):
    if value < self.value:
      if self.leftNode:
        self.leftNode.insertNode(value)
      else:
        self.leftNode = BinarySearchTree(value)
    elif value > self.value:
      if self.rightNode:
        self.rightNode.insertNode(value)
      else:
        self.rightNode = BinarySearchTree(value)

  # 然后是查找的方法。
  def findNode(self, value):
    if self.value == value:
      return self
    elif self.value < value and self.rightNode:
      return self.rightNode.findNode(value)
    elif self.value > value and self.leftNode:
      return self.leftNode.findNode(value)
    return None


def bstSearch(numList, targetNum):
  listLenght = len(numList)
  indexList = [i for i in range(listLenght)]
  indexDic = dict(zip(numList, indexList))
  # print(indexDic)
  root = None
  for _ in indexDic.keys():
    if root == None:
      root = BinarySearchTree(_)
    else:
      root.insertNode(_)
  return root.findNode(targetNum)


"""
6.B-Tree,B树是一种多路查找树，相对于BST，BST的一个节点只能分成最多两个子节点，这样的话整个树的高度就相对较高，而B树是可以控制最多一个节点可以有
  多少个子节点，这样可以有效控制整个树的高度，在查找数据中，树的高低是对效率有很大的影响的。
  并且，所有树的叶子节点都在相同的高度，整个系统的稳定性也可以保证。
  为满足B树的特点，树的构建过程就会比较复杂了。
"""


# 果然，B树的构建是十分复杂的，在网上找到的代码，仿写一遍吧，看看效果，写一个简单的B树，里边只存放数字。
class Entity(object):
  '''数据实体，假设这是一种数据存储的结构'''

  def __init__(self, key, value):
    self.key = key
    self.value = value


# 定义节点，包含了在B树中，所有节点应该有的操作。
class Node():
  def __init__(self):
    self.parent = None
    self.entities = []
    self.children = []

  # 通过一个值，返回存储这个值的实体。
  def find(self, value):
    for i in self.entities:
      if value == i.key:
        return i

  # 删除某个节点中的实体。
  def delete(self, key):
    for i, e in enumerate(self.entities):
      if e.key == key:
        del self.entities[i]
        return (i, e)

  # 判断一个节点是否为叶子节点。
  def isLeaf(self):
    return len(self.children) == 0

  # 添加一个实体，实体添加之后，还要按照实体的key值排序。
  def addEntity(self, entity):
    self.entities.append(entity)
    self.entities.sort(key=lambda x: x.key)

  # 给本节点添加一个叶子节点。
  def addChildNode(self, node):
    self.children.append(node)
    node.parent = self
    self.children.sort(key=lambda x: x.entities[0].key)


class BTree():
  def __init__(self, size=6):
    self.size = size
    self.root = None
    self.length = 0

  def addNode(self, key, value=None):
    # 插入一条数据的话，树的数据长度会+1
    self.length += 1
    # 如果B树为空，即树中还没有数据，则需要创建根节点，并把数据加入进去。
    if not self.root:
      self.root = Node()
      self.root.addEntity(Entity(key, value))
    # 如果不为空，那么就需要利用规则向其中插入数据。
    else:
      point = self.root
      # 在插入实体的时候，要找一个叶子节点插入数据，然后通过数据上浮，即节点分离来做树结构。
      while not point.isLeaf():
        for i, e in enumerate(point.entities):
          if e.key > key:
            point = point.children[i]
            break
          # 证明已经有了该数据，直接在这个index所属的entity上赋新值。
          elif e.key == key:
            self.length -= 1
            e.value = value
            return 0
        if e.key < key:
          point = point.children[-1]
      point.addEntity(Entity(key, value))
      if len(point.entities) > self.size:
        # 如果当前节点的数据值超过了规定的size，那么需要以当前节点为起点，对结构进行调整，即对当前节点进行split。
        self.__split(point)

  def __split(self, node):
    """
    分裂一个节点，规则是将节点的中间值数据移动到父节点，新建一个兄弟右节点，将中间节点的数据移动到新的节点上。
    :param node:
    :return:
    """
    middle = int(len(node.entities) / 2)
    movedEntity = node.entities[middle]
    newNode = Node()
    for e in node.entities[middle + 1:]:
      newNode.addEntity(e)
    if not node.isLeaf():
      for c in node.children[middle + 1:]:
        newNode.addChildNode(c)
    node.entities = node.entities[:middle]
    node.children = node.children[:middle + 1]
    parent = node.parent
    if parent:
      parent.addEntity(movedEntity)
      parent.addChildNode(newNode)
      if len(parent.entities) > self.size:
        self.__split(parent)
    else:
      self.root = Node()
      self.root.addChildNode(node)
      self.root.addChildNode(newNode)
      self.root.addEntity(movedEntity)

  def findValue(self,key):
    if self.__findNode(key):
      return self.__findNode(key).value
    else:
      return "该数据不存在"

  def __findNode(self, key):
    point = self.root
    while not point.isLeaf():
      for i, e in enumerate(point.entities):
        if e.key > key:
          point = point.children[i]
          break
        # 证明已经有了该数据，直接在这个index所属的entity上赋新值。
        elif e.key == key:
          return point
      if e.key < key:
        point = point.children[-1]
    return point.find(key)

  def printTree(self):
    tempList = []
    tempList.append(self.root)
    index = 0
    point = tempList[index]
    while point.children:
      tempList.extend(point.children)
      index += 1
      point = tempList[index]
    for i in tempList:
      for j in i.entities:
        print(j.key, end=' ')
      print(' ', end=' ')


if __name__ == '__main__':
  numList = [9, 4, 6, 8, 2, 1, 0, 3836]
  t = BTree(4)
  t.addNode(20)
  t.addNode(40)
  t.addNode(60)
  t.addNode(70, 'c')
  t.addNode(80)
  t.addNode(85)
  t.addNode(86)
  t.addNode(10)
  t.addNode(30)
  t.addNode(15, 'python')
  t.addNode(75, 'java')
  # t.printTree()
  res = t.findValue(71)
  print(res)
