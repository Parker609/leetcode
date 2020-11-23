"""
剑指 Offer 55 - II. 平衡二叉树
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isBalanced(root: TreeNode) -> bool:
  # 首先定义了一个查看以某一点为root的树的深度的函数。
  def treeDepth(root):
    if not root:
      return 0
    if not root.left and not root.right:
      return 1
    return max(treeDepth(root.left),treeDepth(root.right))+1
  # 遍历所有节点，判断这个节点的左右节点是否一样高就可以了
  res = [True]
  def dfs(root):
    if not root:
      return True
    res[0] = res[0] and (abs(treeDepth(root.left) - treeDepth(root.right))<2)
    if root.left:dfs(root.left)
    if root.right:dfs(root.right)
  dfs(root)
  return res[-1]
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
  res = isBalanced(root)
  print(res)