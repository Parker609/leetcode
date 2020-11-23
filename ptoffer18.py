"""
剑指 Offer 18. 删除链表的节点
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteNode(head,val):
  # 其实就是删除某个节点的操作，常规链表操作。
  point = ListNode("#")
  start = point
  point.next = head
  while point.next:
    if point.next.val == val:
      point.next = point.next.next
    else:
      point = point.next
  return start.next
