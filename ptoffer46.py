"""
剑指 Offer 46. 把数字翻译成字符串

给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。
请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
显然这个问题就是动态规划法，动态规划是有公式的，之后找到公式再说吧
解题的思路其实并不难，假定翻译前i个字符的翻译方法共有f(i)个，那么翻译前i+1个字符就是f(i)+f(i-1)个，前边的f(i-1)是后两个字符符合翻译条件的情况下，
所以接下来函数就好写了，大概，尝试实现一下再说吧。
"""

def translateNum(num):
  """
  测试用例12258
  :param num:
  :return:
  """
  num = str(num)
  if len(num) == 0:
    return 1
  elif len(num) ==1:
    return 1
  dp = [1] * (1+len(num))
  for i in range(2,len(num)+1):
    dp[i] = dp[i-1] + dp[i-2] if int(num[i-2] + num[i-1]) >= 10 and int(num[i-2] + num[i-1]) <= 25 else dp[i-1]
  return dp[-1]



if __name__ == '__main__':
    res = translateNum(12258)
    print(res)