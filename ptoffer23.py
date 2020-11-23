"""
剑指 Offer 24. 反转链表

定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
"""

# 最简单的方法，其实就是简单的栈、队操作反转，并不难。
def reverseList(head):
    if not head:
      return None
    tempStack = [head]
    while head.next:
      tempStack.append(head.next)
      head = head.next
    tempStack[0].next = None
    start = tempStack.pop()
    res = start
    while tempStack:
      temp = tempStack.pop()
      start.next = temp
      start = temp
    return res
