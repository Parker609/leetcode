"""
4. 寻找两个正序数组的中位数
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。

进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？

示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
示例 3：

输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000
示例 4：

输入：nums1 = [], nums2 = [1]
输出：1.00000
示例 5：

输入：nums1 = [2], nums2 = []
输出：2.00000
"""

"""
中位数其实就是中间的那个数，所以首先提出方法1，但是复杂度差不多是n。
"""


def findMedianSortedArrays(nums1: list, nums2: list) -> float:
  # 这边一定要注意，如果数组长度是偶数，那么就需要拿到两个数求平均，下标如果从0开始的话，二者的下标应该是 n/2-1和n/2，奇数的话，下标就是n//2，如果按照位数算的话，就在原本的基础上+1就可以了。
  numsLen = (len(nums2) + len(nums1))
  [counter1, counter2] = [numsLen / 2, numsLen / 2 + 1] if numsLen // 2 == numsLen / 2 else [numsLen // 2 + 1,
                                                                                            numsLen // 2 + 1]
  counter = 0
  tempList = []
  while nums1 or nums2:
    if not nums1 or nums2 and nums1[0] >= nums2[0]:
      counter += 1
      tempList.append(nums2.pop(0))
    elif not nums2 or nums1 and nums2[0] >= nums1[0]:
      counter += 1
      tempList.append(nums1.pop(0))
    if counter == numsLen // 2 + 1:
      break
  return (tempList[int(counter1-1)]+tempList[int(counter2-1)])/2

"""
第二种方法，代码比较简单，就是合并两个数组，排序，然后拿中间值就可以了，因为两个数组本身就是有序的，所以排序就很简单了。
"""
def findMedianSortedArrays2(nums1: list, nums2: list) -> float:
  nums = nums1 + nums2
  nums = sorted(nums)
  numsLen = len(nums)
  [counter1, counter2] = [numsLen / 2, numsLen / 2 + 1] if numsLen // 2 == numsLen / 2 else [numsLen // 2 + 1,
                                                                                             numsLen // 2 + 1]
  return (nums[int(counter1-1)]+nums[int(counter2-1)])/2

if __name__ == '__main__':
  nums1 = [0,1]
  nums2 = [0,1]
  res = findMedianSortedArrays2(nums1, nums2)
  print(res)