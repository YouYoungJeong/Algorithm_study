# 이스케이프 문자 , 특수문자 출력하기
print('"'+r"C:\Download\'hello'.py"+'"')
print('"C:\\Download\\\'hello\'.py"')

''' 
SyntaxError: unterminated string literal
종료 지점을 찾지 못함.
변수 지정하고 출력하면 에러X
'''
# print(r'"C:\Download\'hello'.py"')
msg = r"C:\Download\'hello'.py"
print(f'"{msg}"')
print(r'print("Hello\nWorld")')