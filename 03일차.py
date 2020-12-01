'''
형변환
    데이터의 형태를 변환

    ex) 1->'1'
    str(1) = 정수를 문자열로 형태를 변환

str(데이터) : 문자열로 변환
int(데이터): 정수로 변환
float(데이터): 실수로 변환

>>> float_number=float(100)
>>> type(float_number); print(float_number)
<class 'float'>
100.0

문자열 함수
upper(): 대문자 변경
변수명.upper()

lower(): 소문자 변경 

--> upper, lower 전부 기능이라 저장해야해.

replace(): 문자열 치환(변환) 

split(구분자) : 문자열 나누기   
    리스트로 저장을 한다.

--------------------------------------

리스트 ==(배열, arraylist)
    여러개의 데이터를 한번에 보관할 수 있는 자료형
    []

빈 리스트
>>> list1=[]
>>> type(list1)
<class 'list'>

숫자를 여러개 저장 

list2=[1,2,3,4,5,6,7]

'이서희 20 160.1'

>>> list3=['이서희',20, 160.1]; print(list3); type(list3)
['이서희', 20, 160.1]
<class 'list'>

이서희를 강동원으로 변경 
수정, 변경, 출력할때
리스트명[index번호]

del 리스트명[index]

    ['강동원', 34, 160.1]
    >>> del list3[0]
    >>> list3
    [34, 160.1]

리스트 함수 remove()

리스트 연산 가능 (+, *)
    +는 리스트끼리 연결
    리스트*정수는 반복을 의미
    (단! 문자열하고 실수하고는 곱할수 없다.)

리스트 안에 리스트가 들어가나?

>>> list10=[1,2,3,['다다','라라']]
>>> list10[3][0]
'다다'

>>> practice=['i','am','happy','hungry','sing','want','to','sleep','Are','you','?','!']
2문장 만들기 
    >>> print(practice[0]);print(practice[1]);print(practice[2])
    i
    am
    happy
    >>> practice[0]+practice[1]+practice[2]
    'iamhappy'

리스트 슬라이싱
    리스트명[시작:끝]

str3='201906111014'
    슬라이싱 이용해서
    2019년 year
    06월 month
    11일 day
    10시 14분
    각 각 변수

    그 변수들 이용해서
    2019년 06월 11일 10시 14분 입니다.
    문자열은 변경 X, 슬라이싱을 이용해서 변경한다. 

*내가한거
>>> list2=str3[4:6]; list3=str3[6:8]; list4=str3[8:10]; list5=str3[10:]
>>> print(list1,'년', list2,'월',list3,'일',list4,'시',list5,'분 입니다.')
2019 년 06 월 11 일 10 시 14 분 입니다.


    파이썬 역순으로 데이터를 출력, 변경
    - 값으로 index번호를 지정할 수 있다.
    단! -1부터 시작!
    
0~ 시작: 왼쪽 ->오른쪽
-1 시작: 오른쪽->왼쪽 


리스트 안에 리스트 슬라이싱 가능? 
빈 리스트에 'python' 저장
빈 리스트에는 데이터를 추가할때는 함수 써야해.

append(데이터) : 추가
insert(index, value) : 삽입

remove(value) : 값을 지우는 함수
없는 데이터가 있으면 ValueError 오류 
del(index) : index 위치에 있는 값을 지우는 함수

pop() : 위치에 있는 데이터를 지우는 함수 
삭제되는 데이터를 보여준다.





'''
