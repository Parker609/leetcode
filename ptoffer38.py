"""
剑指 Offer 38. 字符串的排列
输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
"""

"""
解题思路，第一种想法就是全排列，然后再去重就可以了，这么一想好像有点像八皇后问题，递归操作，常规操作。
然后一定要记得去重，重中之重。
"""
def permutation(s: str) -> list:
  resList = []
  resDic = {}
  def dfs(remainS,resS,n):
    if len(remainS) == 0:
      resList.append(resS)
      resDic[resS] = 1
    else:
      for i in range(len(remainS)):
        dfs(remainS[:i]+remainS[i+1:],resS+remainS[i],n+1)
  dfs(s,"",0)
  # print(resDic)
  return (list(resDic.keys()))
  # return resList


"""
第二种方法与第一种方法其实差不多，区别就是对深度优先搜索的剪枝操作的不同，这点是需要注意的。
"""
def permutation2(s: str) -> list:
  resList = []
  def dfs(remainS,resS,n):
    if len(remainS) == 0:
      resList.append(resS)
      print(resS)
      return
    else:
      tempDic = {}
      for i in range(len(remainS)):
        # 在这边加一个判断就可以了，即在相同的位不出现相同的元素。这边维护一个临时dic就可以。
        if remainS[i] in tempDic:
          continue
        tempDic[remainS[i]] = 1
        dfs(remainS[:i]+remainS[i+1:],resS+remainS[i],n+1)
  dfs(s,"",0)
  return resList



if __name__ == '__main__':
    res = permutation2("aba")
    print(res)