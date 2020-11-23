"""
剑指offer第19题，正则表达式匹配。

请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 其中最不要脸的方法，就是直接调用正则表达式re里边的方法，fullmatch方法了解一下。
import re
import numpy as np

# 用魔法打败困难模式。
def isMatch(s, p):
  return re.fullmatch(s, p) != None

# 当然我们还是需要用正规途径来解决这个问题的，主要的方式其实还是使用动态规划法比较合适。
def isMatch2(s,p):
  # 这边设定d[i][j]，二维数组来标记动态规划，用来表示s的前i个字符和p的前j个字符，是互相匹配的。
  # 题目一定要理解正确，这边所说的p代表着pattern，是模式的意思，s里边是没有点（.）或者星（*）的，所以不用考虑s里边如果有点和星号的情况。
  s,p = "#" + s,"#"+p
  lenS = len(s)
  lenP = len(p)
  dp = [[False]*lenP for _ in range(lenS)]
  dp[0][0] = True

  for i in range(lenS):
    for j in range(1,lenP):
      if i == 0:
        dp[i][j] = j>1 and p[j] == "*" and dp[i][j-2]
      elif p[j] in (s[i],"."):
        dp[i][j] = dp[i-1][j-1]
      elif p[j] == "*":
        dp[i][j] = dp[i][j-2] or p[j-1] in (s[i],".") and dp[i-1][j]
      else:
        dp[i][j] = False
  print(np.array(dp))
  return dp[-1][-1]


if __name__ == '__main__':
  res = isMatch2("a", "ab*a")
  print(res)
