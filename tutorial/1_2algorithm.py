# 1. 재귀(Recursive) : 예시 n!
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
print(factorial(5))
print('-'*100)

# 2. 동적(Dynamic) : 예시 피보나치
def fib(n):
    dp = [0, 1]
    
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])

    return dp[n]
print(fib(10))

dp = [0, 1]
# 피보나치 수열 - 결과값
for i in range(2, 10 + 1):
        # print(i)
        dp.append(dp[i - 1] + dp[i - 2])
print(dp)
print('-'*100)

#3. 백트래킹(Backtracking)
def backtrack(path):
    if len(path) == 3:
        print(path)
        return
    for i in range(1, 4):
        if i not in path:
            path.append(i)
            backtrack(path)
            path.pop()
backtrack([])