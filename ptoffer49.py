"""
剑指 Offer 49. 丑数
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
举例：1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数
"""


"""
显然是动态规划法，大概就是这个意思。
这个题比较难的地方就在于对丑数的理解，丑数是只包含2、3、5作为质数的数，那么比方说21就不是丑数，因为里边包含了7这个质数。
所以，就是因为这个原因，某个丑数必然等于之前的某个丑数*2或3或5，那么我们就可以根据这个来搞这个丑数了。
"""
def nthUglyNumber(n: int) -> int:
  dp = [1] * n
  a,b,c = 0,0,0
  for i in range(1,len(dp)):
    dp[i] = min(dp[a]*2,dp[b]*3,dp[c]*5)
    if dp[i] == dp[a]*2:a+=1
    if dp[i] == dp[b]*3:b+=1
    if dp[i] == dp[c]*5:c+=1
  return dp[-1]

if __name__ == '__main__':
    res = nthUglyNumber(10)
    print(res)