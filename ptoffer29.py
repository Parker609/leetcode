"""
剑指 Offer 29. 顺时针打印矩阵
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
"""

"""
有点像马踏棋盘问题的棋盘设定，可以给这个矩阵四周都包上不能踏入的标识，然后碰到之后按照下、左、上、又的顺序改变移动顺序应该就可以了。
"""
import numpy as np

def spiralOrder(matrix: list) -> list:
  rebuidMatrix = np.array([[-1] * (len(matrix[0]) + 2) for i in range(len(matrix)+2)])
  rebuidMatrix[1:1+len(matrix),1:1+len(matrix[0])] = np.array(matrix)
  x,y,flag,counter = 1,1,1,1
  resList = [rebuidMatrix[x,y]]
  rebuidMatrix[x, y] = -1
  flag = 1
  while counter < len(matrix)*len(matrix[0]):
    if flag == 1:
      if rebuidMatrix[x,y+1] != -1:
        y+=1
        resList.append(rebuidMatrix[x,y])
        rebuidMatrix[x, y] = -1
        counter += 1
      else:
        flag = 2
    elif flag == 2:
      if rebuidMatrix[x+1,y] != -1:
        x+=1
        resList.append(rebuidMatrix[x,y])
        rebuidMatrix[x, y] = -1
        counter += 1
      else:
        flag = 3
    elif flag == 3:
      if rebuidMatrix[x,y-1] != -1:
        y-=1
        resList.append(rebuidMatrix[x,y])
        rebuidMatrix[x, y] = -1
        counter += 1
      else:
        flag = 4
    elif flag == 4:
      if rebuidMatrix[x-1,y] != -1:
        x-=1
        resList.append(rebuidMatrix[x,y])
        rebuidMatrix[x, y] = -1
        counter += 1
      else:
        flag = 1
  return resList


if __name__ == '__main__':
  matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
  res = spiralOrder(matrix)
  print(res)