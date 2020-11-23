"""
剑指 Offer 27. 二叉树的镜像
请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
镜像输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""

"""
思路，遍历所有节点，将所有的节点的左右子树对调即可。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def mirrorTree(root: TreeNode) -> TreeNode:
  if not root:
    return root
  root.left,root.right = root.right,root.left
  if root.left:
    mirrorTree(root.left)
  if root.right:
    mirrorTree(root.right)