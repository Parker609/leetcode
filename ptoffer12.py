"""
剑指offer第12题，矩阵中的路径。
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["A","B","c","e"],
["s","F","c","s"],
["a","D","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 刚刚探讨了8皇后问题，显然这个问题也可以用类似的回溯法来解决。
def exist1(board, word):
  """
  判断某个board里边是否存在连续的字母可以凑成当前的word。
  首先默认是board和word都存在的情况。
  :param board:
  :param word:
  :return:
  """
  hight = len(board)
  width = len(board[0])
  wordLenght = len(word)


def checkWord(board, word, path, wordIndex, row, col):
  if wordIndex == len(word):
    print(path)
    # path.pop()
    return True
  if board[row][col] == word[wordIndex]:
    path.append([row, col])
    if row + 1 < len(board) and [row + 1, col] not in path:
      checkWord(board, word, path, wordIndex + 1, row + 1, col)
    if row - 1 >= 0 and [row - 1, col] not in path:
      checkWord(board, word, path, wordIndex + 1, row - 1, col)
    if col < len(board[0]) and [row, col + 1] not in path:
      checkWord(board, word, path, wordIndex + 1, row, col + 1)
    if col >= 0 and [row, col - 1] not in path:
      checkWord(board, word, path, wordIndex + 1, row, col - 1)
  # yield False


# 如果想办法就是当棋盘中存在路径，那么返回True，所以可以把代码稍微更改一下。
def checkWordTrF(board, word, wordIndex, row, col):
  if wordIndex == len(word):
    # path.pop()
    return True
  if not 0 <= row < len(board) or not 0 <= col < len(board[0]) or board[row][col] != word[wordIndex]:
    return False
  # 为了避免走过的路径，可以将路径中走过的位置给换成不可能有的字符。
  board[row][col], temp = "#", board[row][col]
  res = checkWordTrF(board, word, wordIndex + 1, row + 1, col) or checkWordTrF(board, word, wordIndex + 1, row - 1,
                                                                               col) or checkWordTrF(board, word,
                                                                                                    wordIndex + 1,
                                                                                                    row,
                                                                                                    col + 1) or checkWordTrF(
    board, word, wordIndex + 1, row, col - 1)
  board[row][col] = temp
  return res


if __name__ == '__main__':
  board = [["a", "b", "c", "e"],
           ["s", "f", "c", "s"],
           ["a", "d", "e", "e"]]
  path = []
  board2 = [["C","A","A"],["A","A","A"],["B","C","D"]]
  res = checkWordTrF(board2, "AAB", 0, 1, 1)
  print(res)
