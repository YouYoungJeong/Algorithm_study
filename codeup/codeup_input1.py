# 공백으로 두 정수 나누기 
a, b = input().split() # 일반적인 언어에서 지원 X 따로따로 줘야함.
a = int(a); b = int(b)
print(a)
print(b)

# 공백으로 두 문자 나누기
c1, c2 = input().split()
print(c2, c1)

s = input()
print(s, s, s) 

# sprit사용해서 시간분리
a, b = input().split(":")
print(a, b, sep=':')

# 년.월.일 -> 일-월-연도 출력
y, m, d = input().split('.')
print(d,m,y, sep='-')

# 주민번호 - 없이 출력
a,b = input().split('-')
print(a+b)

# 문자열 하나씩 출력
s = input()
for a in range(len(s)):
    print(s[a])

# YYMMDD입력받아 나누어 출력
s = input()
for a in range(0,len(s),2):
    print(s[a]+s[a+1],end=' ')

# 시:분:초 형식으로 시간이 입력될 때 분만 출력
s = input().split(':')
print(s[1])

#알파벳 문자와 숫자로 이루어진 단어 2개를 입력받아
#순서대로 붙여 출력하는 프로그램을 작성
w1, w2 = input().split()
print(w1,w2, sep='')

#정수 2개를 입력받아 합을 출력하는 프로그램을 작성
a , b = a, b = input().split()
c = int(a) + int(b)
print(c)

#실수 2개를 입력받아 합을 출력하는 프로그램을 작성
a, b = input(), input()
c = float(a) + float(b)
print(c)


# 10진수 -> 16진수로 변환(소문자, 대문자)
'''
참고 : notion - 연산자,문자열의 % 포맷방식에 있음
%x로 출력하면 16진수(hexadecimal) 소문자로 출력된다.
(%o로 출력하면 8진수(octal) 문자열로 출력된다.)
'''
a = input()
n = int(a)      
print('%x'% n)
a = input()
n = int(a)      
print('%X'% n)

# 16진수를 입력받아 8진수(octal)로 출력해보자.
a = input()
n = int(a,base=16)  # 16진수로 입력을 받겠다.
print('%o'% n)      # 8진수로 출력
print('%i'% n)      # 10진수로 출력

# 영문자 1개를 입력받아 10진수 유니코드(Unicode) 값으로 출력해보자.
a = ord(input())
print(a)

# 10진 정수 1개를 입력받아 유니코드 문자로 출력해보자.
c = int(input())
print(chr(c))