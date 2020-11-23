"""
剑指 Offer 22. 链表中倒数第k个节点。
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点
开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 这个链表不大好测试，这边直接写一个代码在leetcode上跑来试试。
def getKthFromEnd(head, k):
  # 简单来说，就是双指针，后指针在前指针出发k步之后再出发，等先指针到头之后，后指针指的就是了。
  firstHead = head
  secondHead = head
  counter = 0
  while firstHead and counter != k:
    firstHead = firstHead.next
    counter += 1
  while firstHead:
    firstHead =  firstHead.next
    secondHead = secondHead.next
  return secondHead
