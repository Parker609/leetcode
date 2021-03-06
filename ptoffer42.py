"""
剑指 Offer 42. 连续子数组的最大和
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。
"""

"""
思路分析,这个应该就是比较基本的动态规划法,比方说这个例子(空字串应该算几呢,还是说不允许有空字串,我们先假定不允许空字串):
numList = [-2,1,-3,4,-1,2,1,-5,4]
令f(n)表示以第n个数字结尾的子字符串获得最大值字符串起始的位置和结束的位置.
f(1) = 1,1
f(2) = 2,2
f(3) = 2,2
f(4) = 2,4
... ...
"""

def maxSubArray(nums: list):
  """
  动态规划法最难的地方就是如何书写转移方程,之前的方法转移方程应该就是写错了.
  重新写一遍动态规划.
  状态dp[i]表示最后一位一定是nums[i]的数组列表加和的最大值.
  最后返回dp列表中最大的值就可以了.
  状态转移方程为:
  dp[i-1] < 0: dp[i] = nums[i]
  dp[i-1] > 0: dp[i] = dp[i-1] + nums[i]
  :param nums:
  :return:
  """
  dp = [0] * len(nums)
  dp[0] = nums[0]
  for i in range(1,len(nums)):
    dp[i] = nums[i] if dp[i-1] < 0 else dp[i-1] + nums[i]
  return max(dp)




if __name__ == '__main__':
    res = maxSubArray([8,-19,5,-4,20])
    print(res)
