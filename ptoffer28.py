"""
剑指 Offer 28. 对称的二叉树
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
解题思路一，按照27题做出这个数的镜像树，然后对比每一个节点是否相同，这是一个思路，很简单就不写了，主要说说思路2
解题思路二，给出两个对称点，L和R，如果l.val==r.val and l.left.val==r.right.val and l.right.val == r.left.val，那么就说明这两个点是镜像的。
"""


class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

def isSymmetric(root: TreeNode) -> bool:
  def isMirror(l,r):
    if not l and not r:return True
    if not l and r or not r and l or l.val != r.val:return False
    return isMirror(l.left,r.right) and isMirror(l.right,r.left)
  return isMirror(root.left,root.right)