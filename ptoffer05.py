"""
剑指offer第三题，请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
"""

# 这个题还是很简单的吧，直接python替换就行了。
def replaceSpace(s: str) -> str:
  return s.replace(" ", "%20")

# 其实可以将字符串转换为列表，然后将列表里的空格替换，再合并就ok了，提供个小思路，但是懒得写了。

if __name__ == '__main__':
    sentence = "a b ccc"
    res = replaceSpace(sentence)
    print(res)