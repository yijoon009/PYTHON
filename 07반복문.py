'''
for문
 동일한 명령어 및 비슷한 패턴의 명령어를 반복시켜서
 동작해야할 경우 사용하는 구문
 반복가능한 객체의 요소들의 처음부터 마지막까지
 차례대로 변수에 대입하여 반복문을 수행한다.

for 변수 in 반복가능한 객체:
    반복할 명령문 

반복가능한 객체
(리스트, 튜플, 딕셔너리, 문자열) 

while문의 가독성 좀 떨어진다.
for문 간결하게 반복

while 조건 비교
for문 횟수 반복

1~5까지

list1=[1,2,3,4,5]
for a in list1:
    print(a)


tuple1=('kim','lee','hwang')
#kim님 입장하셨습니다.

for name in tuple1:
    print(name,'님이 입장하셨습니다.')

for str1 in 'hello world':
    print(str1)

#딕셔너리
# 딕셔너리 자체를 반복 key 
dict1={1:'python', 2:'java', 3: 'zython'}

for value in dict1.values():
    print(value)


#딕셔너리
# 딕셔너리 자체를 반복 key
#items()
# key, value 동시에 뽑아오는 내장함수 
dict1={1:'python', 2:'java', 3: 'zython'}
    #[(1,'python'),(2,'java'),(3,'zython')]

for key,value in dict1.items():
    print(key,' ',value)


#딕셔너리
# 딕셔너리 자체를 반복 key
#items()
# key, value 동시에 뽑아오는 내장함수 
dict1={1:'python', 2:'java', 3: 'zython'}
    #[(1,'python'),(2,'java'),(3,'zython')] ()튜플 []리스트 

for key,value in dict1.items():
    print(key,' ',value)
------------------------------------------


range
원하는 숫자의 범위를 객체형식으로 돌려준다.

range(숫자)
 0,1,2,3,4 반복이 가능한 객체
 리스트형태 변경 사용 가능 
 0부터 숫자-1까지

1~5까지 반복이 가능한 객체 생성
 1부터 숫자-1까지 

10부터 50까지 반복하는 객체 생성
 range(10,51)
 
---------------------------------------

1부터 100까지 짝수 홀수합 
각각 저장해서 반복이 끝나면 출력하는 프로그램 

odd=0    #홀수
even=0   #짝수 

for number in range(1,101):
    if number %2==0:
        even+=number
    else :
        odd+=number

print('반복문끝')
print('홀수: ',odd, '짝수: ',even)

구구단 3단 출력 
for number in range(1,10):
    print('3 * ',number,'=',3*number)

    
반복문 실습문제 답!

시험을 치른후 맞은 개수를 알려주는 프로그램

name= input('이름>')
num=int(input('문제 개수>'))

score=0 #총문제 맞춘 개수 저장변수

print('*'*20)

for i in range(1,num+1):
    print(i,'번 문제를 해결했나요?(y/n):')
    ans=input()

    if ans=='y':
        score+=1
    

print('*'*20)
print(name, '학생, 총',score,'문제 해결했습니다.')






'''








 
