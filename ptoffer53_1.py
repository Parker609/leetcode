"""
剑指 Offer 53 - I. 在排序数组中查找数字 I
统计一个数字在排序数组中出现的次数。
"""

"""
思路，遇到再排序数组中查找数字，直接二分法应该是比较快的。
"""

def search(nums: list, target: int) -> int:
  # 程序员竟然忘记二分法怎么写了，略有一丝丝尴尬，哈哈哈哈。
  def binarySearch(nums,target):
    lowIndex = 0
    highIndex = len(nums)-1
    midIndex = (highIndex-lowIndex) // 2
    while lowIndex<=highIndex:
      if nums[midIndex] == target:
        return midIndex
      elif nums[midIndex] < target:
        lowIndex = midIndex+1
        midIndex = lowIndex+(highIndex-lowIndex) // 2
      else:
        highIndex = midIndex-1
        midIndex = lowIndex+(highIndex-lowIndex) // 2
    return -1
  targetIndex = binarySearch(nums,target)
  if targetIndex == -1:
    return 0
  else:
    counter = 1
  pre = 1
  suf = 1
  while targetIndex-pre >= 0 and nums[targetIndex-pre]== nums[targetIndex]:
    counter += 1
    pre += 1
  while targetIndex+suf < len(nums) and nums[targetIndex+suf]== nums[targetIndex]:
    counter += 1
    suf += 1
  return counter
  # counter = 0



if __name__ == '__main__':
    res = search([2,2,3],2)
    print(res)