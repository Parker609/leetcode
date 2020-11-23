"""
剑指 Offer 68 - I. 二叉搜索树的最近公共祖先
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个
节点也可以是它自己的祖先）。”
"""

"""
先说说自己的想法吧,第一个想法就是遍历二叉树,广度有限搜索,并且搜索所有节点的子节点,如果子节点包含给出的两个节点都在这个列表里边,则存储,当找不到的时候,
返回最后一个节点就可以了,那个就是离两个子节点最近的公共祖先.
这边稍微更改一下判定条件,如果两个点都在某个点的同侧节点上,则说明这个点不是最近的公共祖先,再找同侧节点去,否则就是最近公共祖先.
"""


class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
  def bfs(treeNode):
    tempQueue = [treeNode]
    resList = []
    while tempQueue:
      tempNode = tempQueue.pop(0)
      resList.append(tempNode.val)
      if tempNode.left:
        tempQueue.append(tempNode.left)
      if tempNode.right:
        tempQueue.append(tempNode.right)
    return resList
  pValue = p.val
  qValue = q.val
  def lowest(root,p,q):
    leftRes = bfs(root.left)
    rightRes = bfs(root.right)
    if root.val == pValue or root.val == qValue:
      return root
    if (p in leftRes and q in rightRes) or (q in leftRes and p in rightRes):
      return root
    elif p in leftRes and q in leftRes:
      return lowest(root.left,p,q)
    elif p in rightRes and q in rightRes:
      return lowest(root.right,p,q)
  res = lowest(root,pValue,qValue)
  return res
  # tempQueue = [root]
  # while tempQueue:
  #   tempNode = tempQueue.pop()
  #   res = bfs(tempNode)
  #   if tempNode.left:
  #     tempQueue.append(tempNode.left)
  #   if tempNode.right:
  #     tempQueue.append(tempNode.right)
  #   if not(pValue in res and qValue in res):
  #     return tempNode
"""
当然还有更简单的递归写法,之所以说很简单,就是因为代码行数比较少,并且递归操作理解起来其实也挺难的.
"""
def lowestCommonAncestor2(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
  if not root or root.val == p.val or root == q.val:
    return root
  left = lowestCommonAncestor2(root.left,p,q)
  right = lowestCommonAncestor2(root.right,p,q)
  if left and right:
    return root
  elif left and not right:
    return left
  elif right and not left:
    return right



if __name__ == '__main__':
  root = TreeNode(6)
  root.left = TreeNode(2)
  root.right = TreeNode(8)
  root.right.left = TreeNode(7)
  root.right.right = TreeNode(9)
  root.left.left = TreeNode(0)
  root.left.right = TreeNode(4)
  root.left.right.left = TreeNode(3)
  root.left.right.right = TreeNode(5)
  p = TreeNode(2)
  q = TreeNode(4)
  res = lowestCommonAncestor2(root,p,q)
  print(res.val)
