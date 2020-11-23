"""
剑指offer第五题，重建二叉树。根据先序排列和后续排列重建二叉树，做递归就行了。
"""


# 说一下使用先序遍历（根左右）和中序排列（左根右）来重建二叉树的方法，即先序的第一个是树的根，中序是中间的是根，左右分别在左右。
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

# 一言不合就递归，这个递归最合适。
def buildTree(self, pre_order, in_order):
  if len(pre_order) != 0:
    #首先拿到root的key
    root = TreeNode(pre_order[0])
    root_id_in_inorder = in_order.index(root.val)
    root.left = self.buildTree(pre_order[1:1 + root_id_in_inorder], in_order[:root_id_in_inorder])
    root.right = self.buildTree(pre_order[1 + root_id_in_inorder:], in_order[root_id_in_inorder + 1:])
    return root
