"""
剑指 Offer 58 - I. 翻转单词顺序
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"。
"""

def reverseWords(s):
  """
  1.两个方法，运用python的函数，直接切分然后再反转。
  2.其实就是队列和栈的使用，让一个队列中按照某种规则反转过来。
  :param s:
  :return:
  """
  sList = s.strip().split(" ")
  sList.reverse()
  sList = filter(lambda x: x!="",sList)
  s = " ".join(sList)
  return s

def reverseWords2(s):
  # 方法二，使用队列的知识来搞定。
  tempQueue = ""
  tempStack = []
  s = s.strip()
  sLength = len(s)
  pointIndex = 0
  while pointIndex < sLength:
    if s[pointIndex] != " ":
      tempQueue += s[pointIndex]
      pointIndex += 1
    else:
      tempStack.insert(0, tempQueue)
      tempQueue = ''
      while s[pointIndex] == " ":
        pointIndex += 1
  tempStack.insert(0,tempQueue)
  return " ".join(tempStack)

if __name__ == '__main__':
    res = reverseWords2("  hello   world! ")
    print(res)