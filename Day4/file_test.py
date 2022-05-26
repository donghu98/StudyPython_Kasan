# 파일 테스트 

#f = open('C: Repository/StudyPython_Kasan/day4/sample.log. mode='w' , '
# encoding='utf-8'
from fileinput import close


f = open('./day4/sample3.log', mode='w', encoding='utf-8') #상대경로 

f.write('테스트,테스트!!')

f.close()
print('로그파일 생성완료')
