"""
剑指 Offer 53 - II. 0～n-1中缺失的数字
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
"""

"""
其实有多种办法来处理这个题，先说一个思路，这个方法的时间复杂度是N，即做一个等差数列的和，然后依次减去这里边的所有数，最后得到的就是缺失的数。
"""


def missingNumber(nums: list) -> int:
  # 首先先排除特殊情况，即缺失的是最后一个值。
  if nums[-1] == len(nums)-1:
    return nums[-1]+1
  sum_ = (nums[-1]+1)*nums[-1]/2
  sum2 = sum(nums)
  return int(sum_ - sum2)


"""
第二种方法，有人还是使用二分法，毕竟是在有序数列中查找数，二分法的效率还是最高的。
但是二分法中有一些特殊情况难以把控，就还是放弃吧。。。。
"""
def missingNumber2(nums: list) -> int:
  if nums[-1] == len(nums)-1:
    return nums[-1]+1
  if len(nums) == 1:
    return 0
  listLength = len(nums)
  low = 0
  high = listLength - 1
  mid = int(low + (high + low) / 2)
  while low != high-1:
    if nums[mid] == mid:
      low = mid
      mid = int(low + (high - low) / 2)
    else:
      high = mid
      mid = int(low + (high + low) / 2)
  return high
  #   if nums[mid] < nums:
  #     low = mid
  #     mid = int(low + (high - low) / 2)
  #   elif nums[mid] == nums:
  #     return mid + 1
  #   else:
  #     high = mid
  #     mid = int(low + (high + low) / 2)
  # return False



if __name__ == '__main__':
    res = missingNumber2([0])
    print(res)