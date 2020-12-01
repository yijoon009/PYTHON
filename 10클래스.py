'''
클래스
 객체를 정의해 놓은것

클래스 용도
 객체를 생성하는데 사용된다.

객체
 실제로 존재하는 것, 사물 또는 개념.

객체의 용도
 객체의 속성과 기능에 따름

클래스 C언어 구조체 + 함수
        java, c++

사용자 정의 자료형

클래스 : 설계도 (붕어빵틀, 과자틀)
객체 : 실제 물건(붕어빵, 과자)

클래스 생성 방법
 클래스명()  -> 메모리에 할당 하고 객체 생성, 인스턴스
 생 후 주소값을 반환한다. 


class Animal:
    age=0
    name=0

    def cry(self, str1):
        print(self.name,str1,'한다')

#main
a=Animal()

# a 주소를 이용해서 Animal객체에
# 토끼, 3 저장

a.name='토끼'
a.age=3

print(a.age)
print(a.name)


b=Animal()
b.name='강아지'
b.age=1

print(b.name)
print(b.age)

Animallist=[] #빈리스트

Animallist.append(a)
Animallist.append(b)
print(Animallist) <- [<__main__.Animal object at 0x03D0B610>, <__main__.Animal object at 0x03D6C370>] 이렇게 나옴


#id(데이터) 내장함수
# 객체의 주소를 반환하는 함수

클래스 안에 메서드 매개변수 자리는
무조건 self변수 먼저 작성
호출시 호출한 객체 자신이 전달

객체는 인스턴스를 포함
인스턴스는 클래스로부터 생성된 것

클래스 안에서 변수
 클래스 변수:
     모든 인스턴스가 공유
     인스턴스가 생성되기 이전에 이미 메모리공간에 할당되어있다.
 인스턴스 변수:
     인스턴스 변수는 해당 인스턴스만 사용가능
     인스턴스가 생성되는 시점에 메모리공간에 할다오디어있다. 
     
---------------------------------------------

자동차클래스
Car
브랜드명, 가격, 속력, 색상

현대 소나타
4000
240
검은색

Benz s클래스
1억
300
하얀색

각각의 인스턴스를 생성해서 모든 정보 출력 
두 차를 모두 구입 했을 경우의 가격 출력
총 가격: **입니다. 

class Car():
    brand_name=''
    price=0
    speed=0
    color = ''

    #정보출력 메서드
    def info(self):
        print('*'*20)
        print(self.brand_name)
        print(self.price)
        print(self.speed)
        print(self.color)
        print('*'*20)


    
a=Car()
a.brand_name='현대 소나타'
a.price=4000
a.speed=240
a.color='검은색'

a.info()

b=Car()
b.brand_name='Benz S클래스'
b.price=100000000
b.speed=300
b.color='하얀색'
b.info()

print('총 가격: ',a.price + b.price)

--------------------------------------------
class Person:
    name=''
    age=0
    job=''
    hei=0.0
    wei=0
    address=''
    phone=''

    def init(self, name, age, job, hei
             ,wei, address, phone):
        self.name=name
        self.age=age
        self.job=job
        self.hei=hei
        self.wei=wei
        self.address=address
        self.phone=phone
        print('객체 생성 완료!')


이준 = Person()
이준.init('김이준',20,'강사',134.5,40
        ,'서울시 강남구','020-2020-2020')
        
다다=Person()
다다.init('다다',10,'초등생',123.4, 30
        ,'서울 목동','010-1010-1010')




























