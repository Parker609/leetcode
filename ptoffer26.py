"""
剑指 Offer 26. 树的子结构

输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
做这种结构题有点麻烦，因为没办法测试，所以我们先实现一个测试用例，按照给的用例组建一个树结构。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSubStructure(A, B):
  # 直接先序遍历整个A树，和B做对比就可以了，暴力破解啦，首先得找到
  if not B or not A:
    return False
  candidateList = []
  def preOrderTraverse(node):
    if node.val == B.val:
      candidateList.append(node)
    if node.left:
      preOrderTraverse(node.left)
    if node.right:
      preOrderTraverse(node.right)
  preOrderTraverse(A)
  def sameStructure(a,b):
    if not b:return True
    if not a or a.val != b.val:return False
    return sameStructure(a.left,b.left) and sameStructure(a.right,b.right)
  for candidate in candidateList:
    if sameStructure(candidate,B):return True
  return False



if __name__ == '__main__':
    treeNode = TreeNode(3)
    treeNode.left = TreeNode(4)
    treeNode.right = TreeNode(5)
    treeNode.left.left = TreeNode(1)
    treeNode.left.right = TreeNode(2)

    treeTest = TreeNode(4)
    treeTest.left = TreeNode(1)
    res = isSubStructure(treeNode,treeTest)
    print(res)