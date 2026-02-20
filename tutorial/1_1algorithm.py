def main():
    num1 = int(input('첫번째 숫자를 입력하세요:\n'))
    num2 = int(input('두번째 숫자를 입력하세요:\n'))
    opt = int(input('옵션을 선택하세요 -> 1:덧셈, 2:뺄셈, 3:곱셈, 4:나눗셈 \n'))
    
    if opt==1:
        print(f'덧셈 : {num1} + {num2} = {num1 + num2}')
    elif opt==2:
        print(f'뺄셈 : {num1} - {num2} = {num1 - num2}')
    elif opt==3:
        print(f'곱셈 : {num1} * {num2} = {num1 * num2}')
    elif opt==4:
        if num2==0:
            print('0으로 나누기 err')
        else:
            print(f'나눗셈(실수) : {num1} / {num2} = {num1 / num2}')
    else:
        print('옵션 선택 실패')

if __name__ == "__main__":
    main()
