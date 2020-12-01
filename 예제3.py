''' 연필과 펜의 구입하는 개수에 따라 총 가격을 출력하는 프로그램

연필은 1000원, 펜은 2000원
변수 num_pencil, num_pen
이용해서 입력함수를 이용해서 각각 입력받고, 변수 total_price에 저장한다.

출력 상태
연필과  펜의 총 가격은 %% 입니다.
'''
num_pencil=int(input('구입할 연필의 개수를 입력하세요>'))
num_pen=int(input('구입할 펜의 개수를 입력하세요>'))

total_price=num_pencil*1000 + num_pen*2000

print('연필과 펜의 총 가격은 ',total_price, '원 입니다.')
