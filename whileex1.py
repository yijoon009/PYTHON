'''
반복문
 조건이 true인 동안만 반복문 아래 들여쓰기된 부분을 반복해서 수행하세요.

while 조건식:
    참인 경우 실행문장
    ...
    
반복분 3가지
1. 초기식
2. 조건식
3. 증감식 







1부터 5까지 출력 

num=10
while num >0:
    print(num)
    num =num-1
    # num +=1
    

복합연산자
+= -= *= /=

num += 10
num 변수값과 10을 더한다음 num 변수에 저장하세요.



1부터 100까지 반복
그 중에서 홀수만 출력


number=1
while number <101:
    if number %2 ==1:
        print(number)
        number+=2
    
    #print(number)
    #number +=2



반복 횟수를 입력받아서 입력받은 횟수만큼 본인의 이름을 출력하세요!


a=int(input('횟수>'))
s=1
while s <=a:
    print('김이준')
    s +=1
print('while 끝')


무한반복

while True:
    계속반복
    
무한반복을 하다가 어떤 조건 반복을 멈출수 있다.
break

정수를 계속 입력 받다가 0을 입력하면 반복문 종료!

while True:
    s=int(input('정수>'))

    if s==0:
        break

정수를 계속입력하다가 0을 입력하면 반복문 종료!
단!! 입력한 정수의 합을 출력하세요

total=0 #입력정수 합 변수 
while True:
    s=int(input('정수>'))

    if s==0:
        break
    total +=s

print('총 합: ', total)

정수를 무한적으로 입력받다가 5의 배수가 5개 입력되면 반복문을 종료 프로그램 작성

count=0 #개수 

while True:
    s=int(input('정수>'))
    if s%5==0:
        count+=1
        
    if count==5:
        break
---------------------------
count=0 #개수 

while count != 5:
    s=int(input('정수>'))
    if s%5==0:
        count+=1


구구단 3단 출력 9까지 곱한 결과를 출력하세요
3 * 1 = 3

a=1

while a<10:
    print('3 *',a,'=', 3*a)
    a+=1

    
구구단 2단부터 9단까지 곱해서 결과를 출력하는 프로그램을 작성하세요. 
a=1
b=2

while b<10:
    while a<10:
        print(b,'*',a,'=', a*b)
        a+=1
    a=1 #a 초기화하지 않으면 내부반복 X
    b += 1
---------------------------------------
b=2

while b<10:
    a=1
    while a<10:
        print(b,'*',a,'=', a*b)
        a+=1
    
    b += 1
'''















