"""
剑指 Offer 66. 构建乘积数组
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。
"""

"""
这个不能用除法还真的是神仙操作呢,可以稍微研究一下,其实首先完全可以暴力破解,就根据这个公式来写,但是这样时间复杂度很高,不是最优解法.
得通过观察,假如A = [1,2,3,4,5],那么:
B1 = 1 * 2 * 3 * 4 * 5
B2 = 1 * 1 * 3 * 4 * 5
B3 = 1 * 2 * 1 * 4 * 5
B4 = 1 * 2 * 3 * 1 * 5
B5 = 1 * 2 * 3 * 4 * 1
显然,乘积里边其实是一个矩阵,并且可以分为上三角矩阵和下三角矩阵.而且上下三角之间是可以类似动态规划的规则,所以这就给了我们可乘之机.
"""

def constructArr(a:list) -> list:
  listLength = len(a)
  b = [1] * listLength
  for i in range(1,listLength):
    b[i] = b[i-1] * a[i-1]
  temp = 1
  for i in range(listLength-1,0,-1):
    temp = temp * a[i]
    b[i-1] = b[i-1] * temp
  return b


if __name__ == '__main__':
    res = constructArr([1,2,3,4,5])
    print(res)