"""
剑指offer09题，用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除
整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 这边熟悉栈的操作就可以了。
class CQueue:
  def __init__(self):
    self.stack1 = []
    self.stack2 = []
  def appendTail(self,value):
    self.stack1.append(value)
  def deleteHead(self):
    if self.stack1 == []:
      return -1
    while self.stack1 != []:
      self.stack2.append(self.stack1.pop())
    self.stack2.pop()
    while self.stack2 != []:
      self.stack1.append(self.stack2.pop())
    return self.stack1
if __name__ == '__main__':
  cQueue = CQueue()
  cQueue.appendTail("h")
  cQueue.appendTail("e")
  cQueue.appendTail("l")
  cQueue.appendTail("l")
  cQueue.appendTail("o")
  cQueue.deleteHead()
  cQueue.deleteHead()
  cQueue.deleteHead()
  cQueue.deleteHead()
  # cQueue.deleteHead()
  res = cQueue.deleteHead()
  print(res)