"""
红黑树查询，红黑树真的不好理解啊
"""

"""
红黑树的五条性质：
    1)任何一个节点非红即黑；
    2)树的根为黑色；
    3)叶子节点为黑色(注意：红黑树的所有叶子节点都指的是Nil节点)；
    4)任何两个父子节点不可能同时为红色；
    5)任何节点到其所有分枝叶子的简单路径上的黑节点个数相同；
红黑树通过上述五条性质，保证整棵树的黑色节点数量平衡，使得红黑树是一个红黑平衡树，尽可能平衡的二叉树的搜索速度是非常快的。
上亿条数据，通过简单的几十次对比就能找到需要的数据，确实非常厉害了。
"""

class Entity(object):
  '''数据实体，假设这是一种数据存储的结构'''
  def __init__(self, key, value):
    self.key = key
    self.value = value

# 首先定义红黑树的节点
class RBNode():
  def __init__(self,key,value=None,color="R"):
    """
    :param key:
    :param color:默认颜色为红色树
    :param value:
    """
    self.value = value
    self.key = key
    self.color = color
    self.left = None
    self.right =None
    self.parent = None
  def ifBlack(self):
    return self.color == "B"
  def setBlack(self):
    self.color = "B"
  def setRed(self):
    self.color = "R"
  def printSelf(self,node):
    print(node.key,node.color)
    if node.left is not None:
      self.printSelf(node.left)
    if node.right is not None:
      self.printSelf(node.right)



class RBTree():
  """
    红黑树 五大特征
    性质一：节点是红色或者是黑色；
    性质二：根节点是黑色；
    性质三：每个叶节点（NIL或空节点）是黑色；
    性质四：每个红色节点的两个子节点都是黑色的（也就是说不存在两个连续的红色节点）；
  """
  def __init__(self):
    self.root = None

  #树节点的变色操作。
  def changeColor(self,node):
    node.color = "R" if node.color == "B" else "B"


  #定义树的左旋以及右旋操作
  def leftRotate(self,node):
    """
    左旋做了三件事：
         * 1. 将right的左子节点ly赋给node的右子节点,并将node赋给right左子节点ly的父节点(ly非空时)
         * 2. 将right的左子节点设为node，将node的父节点设为right
         * 3. 将node的父节点parent(非空时)赋给right的父节点，同时更新parent的子节点为right(左或右)
    """
    parentNode = node.parent
    rightNode = node.right
    #step1:
    node.right = rightNode.left
    if node.right:
      rightNode.parent = node
    #step2:
    rightNode.left = node
    node.parent = rightNode
    #step3:
    rightNode.parent = parentNode
    if parentNode:
      if parentNode.left == node:
        parentNode.left = rightNode
      else:
        parentNode.right = rightNode
    else:
      self.root = rightNode
  # 定义树中节点的右旋操作。
  def rightRotate(self,node):
    """
    右旋做了差不多的三件事：
         * 1. 将left的右子节点rn赋给node的左子节点,并将node赋给rn右子节点的父节点(left右子节点非空时)
         * 2. 将left的右子节点设为node，将node的父节点设为left
         * 3. 将node的父节点parent(非空时)赋给left的父节点，同时更新parent的子节点为left(左或右)
    """
    parentNode = node.parent
    leftNode = node.left
    # step1:
    node.left = leftNode.right
    if node.left:
      node.left.parent = node
    #step2:
    leftNode.right = node
    node.parent = leftNode
    #step3:
    leftNode.parent = parentNode
    if parentNode:
      if parentNode.left == node:
        parentNode.left = leftNode
      else:
        parentNode.right = leftNode
    else:
      self.root = leftNode
  def treeSearch(self,key):
    """
    红黑树的查找与普通二叉树的查找类似，都是做比较即可。
    :return:
    """
    if not self.root:
      return None
    else:
      point = self.root
      while point != None:
        if point.key == key:
          return point
        elif point.key > key:
          point = point.left
        else:
          point = point.right
      return None

  def insert(self,key,value=None):
    # 插入情景1：当树是空树的时候，二话不说直接插进去，并且将插入的点颜色设置为黑色。
    if not self.root:
      self.root = RBNode(key=key,value=value,color="B")
    else:
      currentpoint = self.root
      nextPoint = currentpoint
      while nextPoint != None:
        if nextPoint.key < key:
          if nextPoint.right == None:
            currentpoint = nextPoint
          nextPoint = nextPoint.right
        elif nextPoint.key > key:
          if nextPoint.left == None:
            currentpoint = nextPoint
          nextPoint = nextPoint.left
        else:
          # 插入情景二：直接将数据插入在nextPoint位置，且该位置节点无需换新的节点，直接替换数据就可以。
          nextPoint.value = value
      else:
        # 在currentPoint处插入数据，是一个新的节点。
        newNode = RBNode(key,value)
        newNode.parent = currentpoint
        if currentpoint.key < key:
          currentpoint.right = newNode
        else:
          currentpoint.left = newNode
        self.rbBalance(newNode)

  #那么问题来了，在插入之后，是一定要做平衡处理的，对node做插入处理。
  def rbBalance(self,node):
    parent = node.parent
    if parent == None:
      node.color = "B"
      return
    if parent.color == "R":
      if node.parent == node.parent.parent.left:
        uncle = node.parent.parent.right
      else:
        uncle = node.parent.parent.left
      if uncle and uncle.color == "R":
        node.parent.color = "B"
        uncle.color = "B"
        uncle.parent.color = "R"
        self.rbBalance(uncle.parent)
      elif parent.parent.left == parent and (not uncle or uncle.color == "B"):
        if parent.left == node:
          parent.color = "B"
          parent.parent.color = "R"
          self.rightRotate(parent.parent)
        elif parent.right == node:
          self.leftRotate(parent)
          self.rbBalance(parent)
      elif parent.parent.right == parent and (not uncle or uncle.color == "B"):
        if parent.right == node:
          parent.color = "B"
          parent.parent.color = "R"
          self.leftRotate(parent.parent)
        elif parent.left == node:
          self.leftRotate(parent)
          self.rbBalance(parent)

  def deleteNode(self,key):
    """
    第一步，找到要删除的点，并找到要删除的这个点的后继节点和这个点互换key和value的值，然后将后继节点删除就可以了。
    在不考虑删除的key和value的情况下，完全可以认为删除的是替换节点。
    :return:
    """
    #找到要删除的节点。
    targetNode = self.treeSearch(key=key)
    if targetNode:
      if not targetNode.left and not targetNode.right:
        if targetNode.parent.left == targetNode:
          targetNode.parent.left = None
        elif targetNode.parent.right == targetNode:
          targetNode.parent.right = None

if __name__ == '__main__':
    rbTree = RBTree()
    rbTree.insert(1)
    rbTree.insert(2)
    rbTree.insert(4)
    rbTree.insert(3)
    rbTree.insert(5)
    rbTree.insert(6,value=123)
    rbTree.insert(7)
    rbTree.root.printSelf(rbTree.root)
    res = rbTree.treeSearch(6)
    print(res.value)

