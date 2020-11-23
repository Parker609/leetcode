"""
剑指offer第二题，在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个
二维数组和一个整数，判断数组中是否含有该整数，如这样的矩阵。

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 这个结构如果站在右上角看的话，其实就是一个二叉树，左侧的数比自己小，下方的数比自己大，就是一个检索二叉树。
def findNumberIn2DArray(matrix, targetnNum):
  # 如果传进来的矩阵是个空矩阵，那么可以直接返回一个False。
  if matrix == []:
    return False
  height = len(matrix)
  width = len(matrix[0])
  # i,j是二叉树的Root的坐标值。
  i = 0
  j = width - 1
  while i < height and j >= 0:
    if matrix[i][j] < targetnNum:
      i += 1
    elif matrix[i][j] > targetnNum:
      j -= 1
    else:
      return True
  return False


if __name__ == '__main__':
  matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
  ]
  targetNum = 225
  res = findNumberIn2DArray(matrix,targetNum)
  print(res)
