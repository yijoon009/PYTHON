'''
함수2

함수 4가지 종류

-입력값 O 반환값 O

def funt1(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

res = funt1(1,2,3)
print('가장 큰 값:',res)

print('가장 큰 값:',funt1(1,2,3))


두개의 수를 받아서 곱해서 돌려주는 함수


-입력값 O 반환값 X
def getM(a,b):    #매개변수 : 전달되는 값을 저장 
    return a*b 

    #return: 함수 종료의미 / 결과값을 main에 반환,
    #return 1개, 반환하는 데이터는 여래가 가능 

#main - 프로그램이 시작하면 가장 처음 호출돼서 명령문들 시작하는 함수

getM(10,10)       #인수 : 함수를 호출할때 전달하는 입력값을 의미


예금계좌
계좌번호, 잔액 

#입금
#돈을 입금하고나면 돌려주는것 X
def deposit(a):
    print(a, '입금했습니다.')

#출금
#출금액 입력 -> 출금액 확인 후 -> 돈을 돌려준다. 
def withdraw(b):
    money=10000
    if money < b:
        return '잔액이 부족합니다.'
    else:
        return b


def account_Check():
    print('잔액조회창입니다.')    

#main
print('*'*20)
print('ATM 기계입니다.')
print('1. 입금')
print('2. 출금')
print('3. 잔액조회')
print('4. 종료')
print('*'*20)

sel = int(input('>'))
if sel==1:
    deposit(10000)

elif sel==2:
    res=withdraw(20000)
    print('출금액:',res)

elif sel==3:
    account_Check()

elif sel==4:
    print('ATM 종료')

else:
    print('선택 오류')

------------------------------------
#호출 순서

def a():
    c=b()
    return c

def b():
    e= d()
    return e

def d():
    return '다다'

#main

a()


---------------------------

-입력 O 반환 X
main에서 정수 하나를 입력받아서
shwNum() 입력받은 정수를 넘겨준다.

showNum: 전달받은 수~100까지 정수 출력 

def showNum(a):
    for i in range(a,101):
        print(i)



number=int(input('정수하나 입력>'))
showNum(number)       
--------------------------------------------
-입력값X 반환값 o

def say():
    return 'hi'

print(say())

#hi=say()
#print(hi)

--------------------------

입력 x 반환 x

def menu():
    print('도움말')
    print('메뉴, 표시')

menu()

-----------------------------

함수 매개변수가 몇개 될지 모를 경우
#가변인자

*매개변수: 여러개 값을 전부 모아서 튜플형식으로 저장
def 함수명(*매개변수):
    <수행할 문장>

def nameShow(*a):
    print(a)

nameShow('dltjgml')
nameShow('rladlwns','dddd')
nameShow('ekek',20,'4232-2323-33')

------------------------------------------
매개변수 미리 초기값 설정
매개변수 값을 초기화해놓으면
매개변수 들어오지 않았을때 설정값으로 함수를 실행한다. 

def nameShow(a='무명씨'):
    print(a)

nameShow()

-----------------------------------
# 한명의 정보를 받아서 출력
# 초기값 설정시 항상 뒤에서부터 작성 

def say_myself(name,age,man=True):
    print('나의 이름은>',name)
    print('나의 나이>',age)

    if man:
        print('남자')
    else:
        print('여자')


say_myself('라라',10,False)
say_myself('디디',12)
--------------------------------------
가변인자 + 초기값 선정  

def funt3(a1,*a2):
    print(a1)

    for i in a2:
        print(i ,'수')
        
funt3('add',1,2,3,4,5)


















