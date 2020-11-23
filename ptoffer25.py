"""
剑指 Offer 25. 合并两个排序的链表
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
"""

# 简单难度，直接上代码，由于链表在编译器里边测试比较麻烦，这边直接写两个有序数组的合并作为测试，最后会修改为leetcode可以识别的代码。
def mergeTwoLists1(l1, l2):
  list1Index = 0
  list2Index = 0
  newList = []
  list1Len = len(l1)
  list2Len = len(l2)
  while list1Index < list1Len -1 and list2Index < list2Len -1:
    if l1[list1Index] <= l2[list2Index]:
      newList.append(l1[list1Index])
      list1Index += 1
    else:
      newList.append(l2[list2Index])
      list2Index += 1
  newList.extend(l1[list1Index:])
  newList.extend(l2[list2Index:])
  return newList


if __name__ == '__main__':
    res = mergeTwoLists1([1,2,3,42,52],[4,6,9,10,44])
    print(res)