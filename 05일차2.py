'''
나이를 입력받아서 버스요금을 계산하는 프로그램 작성
1. 20살 미만은 무료
2. 65세 이상 무료

논리연산자
 and 그리고 :
 or 또는 : 두가지 연산중 하나만 참이 나오면 결과가 참
 
'''

age = int(input('나이입력>'))

if age <20 or age>65:
    print('무료')

else:
    print('정상요금')


'''if~else

두가지 중 하나를 무조건 실행하는 조건문

else 조건식을 작성할수 없다.
else는 if 없이 단독으로 사용 못함
if~else 하나의 세트!

if 조건식:
    참인경우
    ...
else:
    거짓인 경우
    ...
    
'''






'''
score = int(input('점수입력> '))

점수를 입력받아 90이상이면 수!
                80이상이면 우!
                70이상이면 미!

if score >=90:
    print('수')
if score >=80:
    print('우')
if score >=70:
    print('미')

print('if문')




res=score>=60
print(type(res))

if score >=60: #조건이 true, false
    print('합격')
    print('잘하셨습니다.')

print('if문 끝')    
'''
