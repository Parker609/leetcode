"""
关于八皇后问题的一些解法，包括回溯法之类的方法。
八皇后问题其实是一种十分经典的问题，简单来说在8×8的国际象棋棋盘里边，如何摆放8个皇后，用到递归或者动态规划法之类的，是值得研究的问题。
详细介绍可以看看这一篇文章，介绍的十分详细。
https://www.cnblogs.com/franknihao/p/9416145.html
"""


# 方法一，暴力迭代法。
def checkPos(positionArray):
  for i in range(len(positionArray)):
    for j in range(len(positionArray)):
      if i != j:
        if positionArray[i][1] == positionArray[j][1]:
          return False
        elif abs(positionArray[i][0] - positionArray[j][0]) == abs(positionArray[i][1] - positionArray[j][1]):
          return False
  return True


def eightQueen1():
  """
  通过暴力迭代，总共有8的8次方个时间复杂度，反正就是很复杂，虽然以计算机的算力也不算什么，但是确实还是有点意思。
  :return:
  """
  counter = 0
  for a in range(8):
    for b in range(8):
      for c in range(8):
        for d in range(8):
          for e in range(8):
            for f in range(8):
              for g in range(8):
                for h in range(8):
                  positionArray = [[0, a], [1, b], [2, c], [3, d], [4, e], [5, f], [6, g], [7, h]]
                  if checkPos(positionArray):
                    counter += 1
                    print(counter)
                    print(positionArray)
                  # print(counter1)
  # print(counter)


# 方法二，在暴力迭代中去去除那些没有前途的状态，可以节约时间，其实就相当于回溯法。
def eightQueen2():
  """
  通过暴力迭代，总共有8的8次方个时间复杂度，反正就是很复杂，虽然以计算机的算力也不算什么，但是确实还是有点意思。
  :return:
  """
  counter = 0
  positionArray = []
  for a in range(8):
    positionArray.append([0, a])
    if not checkPos(positionArray):
      positionArray.pop()
      continue
    for b in range(8):
      positionArray.append([1, b])
      if not checkPos(positionArray):
        positionArray.pop()
        continue
      for c in range(8):
        positionArray.append([2, c])
        if not checkPos(positionArray):
          positionArray.pop()
          continue
        for d in range(8):
          positionArray.append([3, d])
          if not checkPos(positionArray):
            positionArray.pop()
            continue
          for e in range(8):
            positionArray.append([4, e])
            if not checkPos(positionArray):
              positionArray.pop()
              continue
            for f in range(8):
              positionArray.append([5, f])
              if not checkPos(positionArray):
                positionArray.pop()
                continue
              for g in range(8):
                positionArray.append([6, g])
                if not checkPos(positionArray):
                  positionArray.pop()
                  continue
                for h in range(8):
                  positionArray.append([7, h])
                  if not checkPos(positionArray):
                    positionArray.pop()
                    continue
                  else:
                    counter += 1
                    print(counter)
                    print(positionArray)
                    positionArray.pop()
                  # print(counter1)
                positionArray.pop()
              positionArray.pop()
            positionArray.pop()
          positionArray.pop()
        positionArray.pop()
      positionArray.pop()
    positionArray.pop()


# 方法三，上边的代码可读性比较强，但是有很多重复的代码，虽然表达了回溯的想法，但是代码量太大，并且只能针对八皇后问题，相当于将此类问题写死了，所以下边我们整理一版代码，递归回溯方法。
def checkBoard(board, row, colume):
  for i in range(row):
    if abs(colume - board[i]) in (0, abs(row - i)):
      return False
  return True

def printBoard(board):
  '''为了更友好地展示结果 方便观察'''
  import sys
  for i, col in enumerate(board):
    sys.stdout.write('□ ' * col + '■ ' + '□ ' * (len(board) - 1 - col))
    print("")

def eightQueen(board, row):
  """
  在进入递归时，应当传入的递归参数显然是期盼状态以及所应当到达的位置
  :param board: 期盼状态
  :param row: 应当摆放的棋子行数
  :return:
  """
  # 如果应当摆放的位置是第9行，那么说明摆放成功。
  if row == 8:
    print(board)
    printBoard(board)
    # return True
  for colume in range(8):
    if checkBoard(board, row, colume):
      board[row] = colume
      eightQueen(board, row + 1)
  return False

if __name__ == '__main__':
  state = [-1]*8
  print(state)
  eightQueen(state,0)
  # positionArray = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
  # res = checkPos(positionArray)
  # print(res)
