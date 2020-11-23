"""
剑指 Offer 59 - I. 滑动窗口的最大值
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
"""

"""
先尝试一下简单的动态规划,不过这边需要考虑滑动窗口里边第一个位置的那个值,看是不是最大的值.
"""


def maxSlidingWindow(nums: list, k: int) -> list:
  numsLength = len(nums)
  dp = [0] * (numsLength + 1 - k)
  dp[0] = max(nums[:k])
  for i in range(len(dp)-1):
    if nums[i] == dp[i]:
      if nums[i+1]>dp[i]:
        dp[i+1] = nums[i+1]
      else:
        dp[i+1] = max(nums[i+1:i+k+1])
    else:
      dp[i+1] = max(dp[i],nums[i+k])
  return dp

if __name__ == '__main__':
    res = maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)
    print(res)