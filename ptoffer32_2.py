"""
剑指 Offer 32 - II. 从上到下打印二叉树
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
不过要求同一层的要输出在同一个List中。
"""

# 思路，对二叉树简单的层序遍历。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def levelOrder(root):
  # 层序遍历，简单来说就是栈和树的搭配。
  tempQueue = [root]
  tempList = []
  while tempQueue:
    # 这边做一个计数应该就可以达到想要的效果。
    teList = []
    counter = 0
    layerLength = len(tempQueue)
    while counter<layerLength:
      point = tempQueue.pop(0)
      teList.append(point.val)
      if point.left:
        tempQueue.append(point.left)
      if point.right:
        tempQueue.append(point.right)
      counter += 1
    if teList:
      tempList.append(teList)
  return tempList

if __name__ == '__main__':
  if __name__ == '__main__':
    treeNode = TreeNode(3)
    treeNode.left = TreeNode(4)
    treeNode.right = TreeNode(5)
    treeNode.left.left = TreeNode(1)
    treeNode.left.right = TreeNode(2)
    res = levelOrder(treeNode)
    print(res)
    treeTest = TreeNode(4)
    treeTest.left = TreeNode(1)
