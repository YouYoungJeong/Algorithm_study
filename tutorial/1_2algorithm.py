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

# 3. 백트래킹(Backtracking)
def backtrack(path):
    if len(path) == 3:
        print(path)
        return
    for i in range(1, 4):
        if i not in path:
            path.append(i)            
            backtrack(path) # 재귀
            path.pop()
backtrack([])

def backtrack(path, depth=0):
    print("  " * depth, f"[ENTER] path={path}")

    if len(path) == 3:
        print("  " * depth, f"[PRINT] {path}")
        return

    for i in range(1, 4):
        print("  " * depth, f"for 시작 → i={i}, path={path}")

        if i not in path:
            print("  " * depth, f"append({i})")
            path.append(i)

            backtrack(path, depth+1)

            print("  " * depth, f"pop() 실행 전 path={path}")
            path.pop()
            print("  " * depth, f"pop() 후 path={path}")

    print("  " * depth, f"[EXIT] path={path}")
backtrack([])
print('-'*100)

# 4. 분할 정복(Divide and Conquer): Merge Sort(병합정렬)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # 슬라이싱 + 재귀때문에 
    # len=1이 될때까지 쪼개짐, 결과는 값이 1개씩 있는 리스트값이 나옴
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result
print(merge_sort([5,2,8,1,4,6]))
print('-'*100)

# 5. 탐욕(Greedy)
def greedy_change(money):
    # 문제기준 큰수가 먼저 앞으로 있어야함 정렬 중요!
    coins=[500, 100, 50, 10] 
    count = 0
    for coin in coins:
        count += money // coin
        money %= coin
    return count
print(greedy_change(1260))
print('-'*100)

# 6. 완전탐색(Brute Force)
nums = [1,2,3,4]
for a in nums:
    for b in nums:
        if a + b == 5:
            print(a, b)
print('-'*100)

# 7. 랜덤알고리즘(Randomized)
import random
def random_search(arr):
    while True:
        # 인덱스값 0~3 까지의 정수값을 찍어서 값이 7 이 나오면 그 인덱스 번호 출력
        idx = random.randint(0, len(arr)-1)
        if arr[idx] == 7:
            return idx
print(random_search([1,4,7,9]))
