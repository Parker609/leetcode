"""
剑指 Offer 20. 表示数值的字符串
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，
但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。
"""


"""
这个题其实还是挺难的，解题分析其实就是有限状态机的复杂使用，复杂编程的时候可以考虑画这个图，好记性不如烂笔头嘛。
如果这么考虑的话，就需要做状态判断，字符串自左向右总共有如下的状态，其实通过阅读数字做一个树状图应该会好很多吧，试试试试：
字符类型大概有：空格「 」、数字「 0—9 」、正负号「 +− 」、小数点「.」、幂符号「eE」。
1. 空格 --> 转移2或3
2. 数字 --> 转移4或5
3. 正负号 --> 转移2
4. 点dot --> 转移6
5. 幂符号 --> 转移7或8
6. 数字2 --> 转移5
7. 正负号2 --> 转移8
8. 数字2 结束.
大概这么8个状态,是通过状态转化图或者说是状态图得出来的.
"""

# 这个算法先保留,如果有任何错误的地方,说明是因为状态没有全部选对,肯定会有问题的,比方说".1"这个数,就没有考虑进去.
def isNumber(num: str) -> bool:
  state = {
    "1":{"b":"1","dig":'2',"s":'3'},
    "2":{"dig":'2',"dot":'4',"e":'5'},
    '3':{"dig":'2'},
    '4':{"dig":"6"},
    "5":{"s":"7","dig":"8"},
    "6":{"e":"5"},
    "7":{"dig":"8"},
    "8":{"dig":"8"}
  }
  num = " "+num.strip()
  thisState = "1"
  numLength = len(num)
  if numLength == 1:
    return False
  pointIndex= 1
  while pointIndex < numLength:
    if '0' <= num[pointIndex] <= '9':
      t = 'dig'  # digit
    elif num[pointIndex] in "+-":
      t = 's'  # sign
    elif num[pointIndex] in "eE":
      t = 'e'  # e or E
    elif num[pointIndex] in ".":
      t = "dot"  # dot
    elif num[pointIndex] == " ":
      t="b"
    thisState = state[thisState].get(t)
    if thisState:
      pointIndex += 1
      continue
    return False
  return True


# 先写一个搞笑的写法，不谈算法，直接做转换，直接试一试能不呢个把这个给出的数转换成数字，用float这个函数捕捉catch就可以了。
def isNumber1(num):
  try:
    float(num)
  except:
    return False
  return True

if __name__ == '__main__':
  res = isNumber(" ")
  print(res)