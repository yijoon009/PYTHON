'''영한사전 만들기
영어를 입력하면 그에대한 한글로 답출력


단어를 입력하세요> cat


cat->고양이 출력
딕셔너리 animallist


cat
rabbit
puppy

sparrow가 영햔사전에 있니? 결과 출력 '''

animallist={'cat':'고양이','rabbit':'토끼','puppy':'강아지'}

a= input('단어를 입력하세요>')
print(animallist[a])

print('sparrow가 영한사전에 있니?','sparrow' in animallist)
