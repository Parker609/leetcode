"""
剑指 Offer 48. 最长不含重复字符的子字符串
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
"""

"""
解题思路，动态规划
考虑一下，dp[i]表示使用s[i]结尾的字符串所包含的最长不重复字符子串。
转移方程：dp[i] = dp[i-1]+1 (最后一个字符和之前的情况没有重复的情况)
        dp[i] = max(dp[i-1],j-i)
"""

def lengthOfLongestSubstring(s):
  sLength = len(s)
  dp = [0] * (sLength+1)
  dp[1] = 1
  recordDict = {s[0]:1}
  firstIndex = 0
  for i in range(2,sLength+1):
    if s[i-1] not in recordDict:
      dp[i] = dp[i-1]+1
    else:
      firstIndex = recordDict[s[i-1]] if recordDict[s[i-1]] > firstIndex else firstIndex
      dp[i] = (i-firstIndex)
    recordDict[s[i-1]] = i
  return dp


if __name__ == '__main__':
    res = lengthOfLongestSubstring("abba")
    print(res)