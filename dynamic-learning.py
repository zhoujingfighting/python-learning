'''
学习动态规划
'''

# 第一题当然是经典的斐波那契数列
# dp = [0,1]
def fibonacci(n):
  dp = [0,1]
  if n<0:
    print("n can not be less than zero")
  for i in range(2,n+1):
    dp.append(dp[i-1]+dp[i-2])
    # 区别于js和c++的动态数组,py好像不能动态
  return dp[n]

print(fibonacci(10))
# print(dp)

