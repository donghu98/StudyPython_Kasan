import os

PRJ_root = os.path.dirname(os.path.abspath(__file__)) 
print(PRJ_root)   # py 파일이 위치한 경로

Base_Dir = os.path.dirname(PRJ_root)  #DAY5의 가장 기본이 되는 장소가 어디냐 
print(Base_Dir)   # 프로젝트 기반 폴더 경로 

f = open('./test_console.txt', mode='w', encoding='utf-8')
f.write('Hello world/n')
f.close()