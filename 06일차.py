'''
if 조건식:
    참인경우 실행
elif 조건식:
    참인경우 실행
elif 조건식:
    참인경우 실행
else:
    거짓인경우 실




'''
'''
8세 미만 , 65세 이상 무료
8 이상 13세 이하 300원
14이상~16 이하 500원
17이상 19이사 700원
20이상 정상요금 
'''

age = int(input('나이>'))
if age<8 or age>=65:
    print('무료')
elif age<=13:
    print('300원')
elif age<=16:
    print('500원')
elif age <=19:
    print('700원')
else:
    print('정상요금')















