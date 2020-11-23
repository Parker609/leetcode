"""
剑指 Offer 39. 数组中出现次数超过一半的数字
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。
"""

"""
一言不合暴力破解，走一遍就行了，记住用hash表来记住这个值。
"""

def majorityElement( nums: list) -> int:
  hash = {}
  for i in nums:
    if i not in hash:
      hash[i] = 1
    else:
      hash[i]+=1
  for i in hash:
    if hash[i] > len(nums)//2:
      return i

"""
虽然这个题是简单题，但是可以提出多种算法，还是有值得学习的地方的。
方法2，将数组排队，处于中间位置的数字一定是众数，切记，这个题说了众数是多余一半的，所以一定能得到。
"""
def majorityElement2( nums: list) -> int:
  nums = sorted(nums)
  return nums[len(nums)//2]

"""
第三种方法，是最为有意思的，被称作摩尔投票法，就是用来统计最多的那个票是谁。
摩尔投票的用以在于假定第一个数是最多的数，如果碰到了相同的数就vote+1，否则就-1，稍微一理解就明白了，把这个东西的道理复制下来就明白了。
摩尔投票法：
设输入数组 nums 的众数为 xx ，数组长度为 nn 。

推论一： 若记 众数 的票数为 +1+1 ，非众数 的票数为 -1−1 ，则一定有所有数字的 票数和 > 0>0 。

推论二： 若数组的前 aa 个数字的 票数和 = 0=0 ，则 数组剩余 (n-a)(n−a) 个数字的 票数和一定仍 >0>0 ，即后 (n-a)(n−a) 个数字的 众数仍为 xx 。

作者：jyd
链接：https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/solution/mian-shi-ti-39-shu-zu-zhong-chu-xian-ci-shu-chao-3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

def majorityElement3( nums: list) -> int:
  vote = 1
  candidate = nums[0]
  for i in range(1,len(nums)):
    if vote == 0:
      candidate = nums[i]
      vote += 1
      continue
    if nums[i] == candidate:
      vote += 1
    else:
      vote -= 1
  return candidate

if __name__ == '__main__':
    res = majorityElement3( [10,9,9,9,10])
    print(res)