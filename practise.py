"""
这其实就是一个联系用的文档，试试写一个快排和堆排算法，这算是排序算法里边性能比较高的两个算法。
"""


# 快速排序，其实就是快速的找到某个位置的数字（元素）应该在的位置，通过递归的方式来实现这个代码。
def quickSort(numList):
  if len(numList) < 2:
    return numList
  lowPoint = 0
  highPoint = len(numList) - 1
  tempNum = numList[0]
  while lowPoint != highPoint:
    while lowPoint != highPoint and numList[highPoint] > tempNum:
      highPoint -= 1
    numList[lowPoint] = numList[highPoint]
    while lowPoint != highPoint and numList[lowPoint] < tempNum:
      lowPoint += 1
    numList[highPoint] = numList[lowPoint]
  return quickSort(numList[:lowPoint]) + [tempNum] + quickSort(numList[lowPoint + 1:])


# 堆排，堆排里边比较复杂的，其实是构建堆和堆调整，其实树是可以用数组来表示的，
def justifyHeap(arr, i):
  if 2*i+1 < len(arr) and arr[i] < arr[2 * i + 1]:
    temp = arr[i]
    arr[i] = arr[2 * i + 1]
    arr[2 * i + 1] = temp
  if 2*i < len(arr) and arr[i] < arr[2 * i]:
    temp = arr[i]
    arr[i] = arr[2 * i]
    arr[2 * i] = temp

def heapSort(arr):
  temList = []
  arr.insert(0,"#")
  while len(arr)!=1:
    lenArr = len(arr)
    startPoint = lenArr//2
    for i in range(startPoint,0,-1):
      justifyHeap(arr,i)
    temList.append(arr.pop(1))
  return temList




if __name__ == '__main__':
  # numList = [3, 2, 5, 7, 1, 10, 33, 21]
  # res = quickSort([3, 2])
  # print(res)
  res = heapSort([1,2,333,42,11111])
  print(res)