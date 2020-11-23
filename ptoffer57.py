"""
剑指 Offer 57. 和为s的两个数字
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。
"""

"""
解题思路，当然可以暴力破解，从头到尾做两个循环的嵌套操作，暴力破解，但是这是下下策，毕竟是算法题，肯定是得思考一下有没有更好的办法。
题目中给出了是一个递增数列，可以从这边作为切入点进去。
从左向右数递增，那么从右向左数字递减，这样的话，双指针就是最简单的办法了。
"""

def twoSum(nums: list, target: int) -> list:
  startPoint = 0
  endPoint = len(nums)-1
  while startPoint != endPoint:
    if nums[startPoint] + nums[endPoint] < target:
      startPoint += 1
    elif nums[startPoint] + nums[endPoint] > target:
      endPoint -= 1
    else:
      return [nums[startPoint],nums[endPoint]]
  return []

if __name__ == '__main__':
    res = twoSum(nums = [10,26,30,31,47,60], target = 40)
    print(res)