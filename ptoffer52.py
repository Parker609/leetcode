"""
剑指 Offer 52. 两个链表的第一个公共节点
输入两个链表，找出它们的第一个公共节点。
"""


class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None


"""
思路其实很简单，大概是有两个方法，先说第一种，就是让两个链表尾端对齐，然后从头向后一起捋，就能找到了，大概时间复杂度是2n，其实就是n。
"""


def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
  ahead, bhead = headA, headB
  while ahead.val != bhead.val:
      ahead = ahead.next if ahead else headB
      bhead = bhead.next if bhead else headA
  return ahead

"""
第二种就是把Y字变成8字，相当于让两个人在不同长度的两个圈内跑，一直跑到两个人都在出口，提供个思路，代码可以之后自己实现。
"""