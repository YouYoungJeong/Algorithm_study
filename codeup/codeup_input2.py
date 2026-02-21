# 입력된 정수의 부호를 바꿔 출력
n = int(input())
print(-n)

# 문자 1개를 입력받아 그 다음 문자를 출력해보자.
a = input()
n = ord(a) # 문자열 유니코드 정수로 변환
print(chr(n+1)) # 유니코드정수 + 1 하면 다음 정수 출력
print(a, n)

# 정수 2개(a, b)를 입력받아 a에서 b를 뺀 차를 출력하는 프로그램을 작성
#(2개의 정수가 공백으로 구분되어 입력된다.)
a, b = input().split()
print(int(a) - int(b))

# 실수 2개(f1, f2)를 입력받아 곱을 출력하는 프로그램을 작성
# 2개의 실수가 공백으로 구분되어 입력된다.
a, b = input().split()
print(float(a) * float(b))

# 단어와 반복 횟수를 입력받아 여러 번 출력해보자.
# 단어와 반복 횟수가 공백으로 구분되어 입력된다.
w, n = input().split()
print(w * int(n))

# 반복 횟수와 문장을 입력받아 여러 번 출력
# 반복 횟수와 문장이 줄을 바꿔 입력된다.
n = int(input())
s = input()
print(n * s)

#정수 2개(a, b)를 입력받아 a를 b번 곱한 거듭제곱을 출력하는 프로그램을 작성
# 2개의 정수(a, b)가 공백으로 구분되어 입력된다.
a, b = input().split()
print(int(a) ** int(b))

# 6039 - 실수 2개(f1, f2)를 입력받아 f1을 f2번 거듭제곱한 값을 출력하는 프로그램을 작성
# 2개의 실수(f1, f2)가 공백으로 구분되어 입력된다.
f1, f2 = input().split()
print(float(f1) ** float(f2))