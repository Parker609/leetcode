"""
剑指offer第四题，输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 目前的思路是循环整个链表，然后在List中从头插入值就可以了。
def reversePrint(self, head: ListNode):
  if head == None:
    return []
  temp_list = []
  node = head
  temp_list.append(node.val)
  while node.next != None:
    node = node.next
    temp_list.insert(0, node.val)
  return temp_list