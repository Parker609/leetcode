"""
1. 两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""
"""
首先给数组排序，然后用左右双指针的办法来捋就可以了。
"""


def twoSum(num: list, target: int) -> list:
  nums = sorted(num)
  left = 0
  right = len(nums)-1
  while nums[left]+nums[right] != target:
    if nums[left]+nums[right] < target:
      left += 1
    else:
      right -= 1
  return [num.index(nums[left]),len(num) - list(reversed(num)).index(nums[right])-1]

"""
上述方法在返回值上还是需要处理的，这边再提出一种方法，就是利用差值的哈希表。
"""
def twoSum2(nums: list, target: int) -> list:
  hashDic = {}
  for i in range(len(nums)):
    if target - nums[i] not in hashDic:
      hashDic[nums[i]] = i
    else:
      # print([hashDic[nums[i]],i])
      return [hashDic[target-int(nums[i])],i]


if __name__ == '__main__':
  nums = [2,7,11,15]
  res = twoSum2(nums,9)
  print(res)
