"""
剑指 Offer 33. 二叉搜索树的后序遍历序列
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
"""
"""
呵呵哒。。。之前的看来是我眼瞎了，是给一个数组，判断这个数组是否是一个二叉搜索树的后续遍历结果，那么一定要考虑二叉搜索树的特点，那就是左>根>右。
并且，针对这个特点，数组最右边的值是根，可以用这个值把数组分成两部分。
"""
def verifyPostorder(postorder: list) -> bool:
  if not postorder:
    return True
  root,left,right,state = postorder[-1],[],[],0
  while True:
    if postorder[state] < root:
      left.append(postorder[state])
      state += 1
    else:
      break
  while True:
    if postorder[state] > root:
      right.append(postorder[state])
      state += 1
    else:
      break
  if state == len(postorder)-1:
    return verifyPostorder(left) and verifyPostorder(right)
  else:
    return False
if __name__ == '__main__':
    res = verifyPostorder([1,3,2,6,5])
    print(res)