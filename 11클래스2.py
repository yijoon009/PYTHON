'''
not 연산자
~이 아니다!

not true : 참이 아니다. -> 결과 거짓
not flase : 거짓이 아니다 -> 결과 참


tv 클래스
특징, 기능

색깔, 전원상태(on/off), 채널
채널up, 채널down

참이면 tv on / 거짓 off

class Tv:
    brand_name=''
    color=''
    power=False
    channel=10

    def init(self,name, color,  channel):
        self.brand_name=name
        self.color=color
        self.channel=channel
        print('Tv')
    
    #입력 X 반환 X
    def power():
        not power

    def channelUp():
        channel+=1

    def channelDown():
        channel-=1

samsung=Tv()
samsung.init('삼성Tv','하얀색',2)

lg=Tv()
lg.init('lg TV','하얀색',5)
------------------------------------------

생성자
 객체를 생성할 때 자동적으로 인스턴스 변수를 초기화
 객체를 생성할때 가장먼저 실행 
 객체를 생성할때 기본적으로 생성자를 1개씩 가지고있다. 

def __init__(self):
    pass, 명령문!

기본생성자
 클래스를 작성할 때 컴파일할때 컴파일이 작성해준다.
 
예)
class A:
    #빈클래스
    #기본생성자
    def __init__(self):
        print('A')

    pass

A()
---------------------------------------

생성자를 이용해서 인스턴스변수 생성
계좌명, 계좌번호, 잔액
비밀번호

입금, 출금, 예금조회

class Account:
    def __init__(self, name, num, money,pw):
        self.acc_name=name
        self.acc_num=num
        self.acc_balance=money
        self.acc_pw=pw
        print('계좌등록 ok')

    #출금
    #입력ㅇ 반환 o
    def with1(self, money):
        if money <=self.acc_balance:
            self.acc_balance -=money
            return money
        else:
            return '잔액부족'

    #입금 
    #입력값 O 반환값 X 
    def posit(self,money):
        self.acc_balance +=money
        print('입금액: ', money)
        


영희=Account('영희계좌','1111',10000,1234)
print(영희.acc_name)
영희.posit(20000)
print('출금: ',영희.with1(50000))

---------------------------------------------------

소멸자
 객체가 소멸(삭제)할때 호출되는 메서드 

class B:
    def __init__(self):
        print('객체 생성')

    def __del__(self):
        print('객체 소멸')

b1=B()  #객체 생성됐다.
del b1  #del 이용해서 지우면 객체 소멸 출력
        #pass: 아무것도 출력 X

------------------------------------------------

상속
 물려받는 기능
 기본 클래스로부터 기능을 받아서 새로운 클래스를 작성

부모클래스 자식클래스
기본클래스 파생클래스
상위클래스 하위클래스 

변수, 메서드,생성자 물려받는다.
부모클래스의 멤버의 개수보다 자식클래스의 멤버개수가
적을수 없다.

-------------------------------------------------------

class 클래스명(상속받을 클래스명)

#기본 캐릭터
class Character:
    def __init__(self, id1='무명씨', hp=0,mp=0):
        self.id1=id1
        self.hp=hp
        self.mp=mp

    def info(self):
        print(self.id1)
        print(self.hp)
        print(self.mp)

    def at(self):
        print('기본공격')

#전사
class Warrior(Character):
    pass

#마법사
class Wizard(Character):
    pass

#궁수
class Archer(Character):
    pass

class Monster(Character):
    pass


w1=Warrior('오빠')
w1.at()

m1=Monster('오크',100,100)
m1.info()

----------------------------------------
평균클래스
평균을 내는 기능

총점클래스
총점을 저장하는 변수
총점을 계산하는 기능

class Avg:
    def __init__(self):
        self.avg=0
        

    def average(self,total):
        self.avg=self.total/3
        print('평균은',self.avg)

class Total(Avg):

    def total(self,kor,math,eng):
        self.kor=kor
        self.math=math
        self.eng=eng
        self.total=kor+math+eng

        self.average(self.total)

person1=Total()
person1.total(92,92,92)

----------------------------------------------

교수,어린이,학생
->사람->먹고 놀고 자고 기능

기본클래스 (부모클래스)

class Person:
    def __init__(self,name,age,job):
        self.name=name
        self.age=age
        self.job=job

    def eat(self):
        print(self.name,'님이 먹는다.')

    def sleep(self):
        print(self.name,'님이 잔다.')

    def play(self):
        print(self.name,'님이 논다.)

    def del(self):
        print('긱체가 소멸합니다.')
        
class Child(Person):
    pass

class Student(Person):
    pass

class Professor(Person):
    pass


------------------------------------------------

신용카드
 
놀이동상 50% 할인
영화 몇회 무료
쇼핑 30%
교통카드
 

class Trans_card:
    pass

class Shopping:
    pass

class Movie:
    pass

class Park: #놀이동산
    pass


class Card:
    def __init__(self,name,pw,number):
        self.name=name
        self.pw=pw
        self.number=number
        print('카드생성완료')

    def pay(self):
        print('결제합니다.')

#다중 상속
#클래스들끼리 여러개를 상속받을 수 있다
#class 클래스명(상.클1, 상.클2, ...)
        
#삼성카드 -> 쇼핑,교통
class Samsung_Card(Card,Shopping, Trans_card):
    pass

#롯데카드 ->영화
class Lotte_Card(Card,Movie):
    pass

#kb카드 ->결제
class Kb_Card(Card):
    pass














