"""
剑指offer第14-1题，剪绳子。
本题和offer第14-2问题一样。
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 其实这个问题是个很神奇的问题，第一反应是动态规划法。
def countRope(n):
  if n == 1:
    return False
  if n == 2:
    return 1
  if n == 3:
    return 2
  # 遍历dp数组。
  dp = [0] * (n + 1)
  dp[1] = 1
  dp[2] = 2
  dp[3] = 3
  for i in range(4, n + 1):
    for j in range(1, i//2+1):
      dp[i] = max(dp[i], dp[j] * dp[i - j])
  return dp[n]


if __name__ == '__main__':
  res = countRope(5)
  print(res)
