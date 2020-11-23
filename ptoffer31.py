"""
剑指 Offer 31. 栈的压入、弹出序列
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是
某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。
"""

"""
基本思路就是对压入栈和弹出栈做对比,看压入的能否弹出就可以了,不过感觉代码会比较复杂.
"""

def validateStackSequences(pushed: list, popped: list) -> bool:
  # 就两个队列或者说栈之间找麻烦呗.
  # pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
  tempStack = []
  for i in pushed:
    tempStack.append(i)
    while tempStack and tempStack[-1] == popped[0] :
      tempStack.pop()
      popped.pop(0)
  if popped:
    return False
  else:
    return True

if __name__ == '__main__':
  res = validateStackSequences([1,0],[1,0])
  print(res)