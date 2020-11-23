"""
剑指 Offer 50. 第一个只出现一次的字符
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
"""


# 简单来说，就是简单的哈希表。
def firstUniqChar(s):
  hashDict = {}
  sLength = len(s)
  for i in range(sLength):
    if s[i] not in hashDict:
      hashDict[s[i]] = i
    else:
      hashDict[s[i]] = -1
  res = sorted(hashDict.items(),key=lambda items:items[1])
  for item in res:
    if item[1]!= -1:
      return item[0]

if __name__ == '__main__':
    res = firstUniqChar("abccccc")
    print(res)