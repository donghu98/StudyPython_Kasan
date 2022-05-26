'''
주소록 프로그램 v1.1
작성일 2022-05-26 14:14
작성자 쩔받은로또
설명 파일DB를 사용한 주소록 프로그램 테스트
''' 
import os
from posixpath import split
# 주소록 클래스


class Contact :
    name = ''; phone_number = ''; e_mail = ''; addr = ''

    # 생성자(constructor) 
    def __init__(self, name, phone_number, e_mail, addr) -> None: ## None : 리턴값이 존재하지 않는다 
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr
    
    def __str__(self) -> str:   #string : 문자열  
        res_str = f'이름 : {self.name}\n' \
        f'폰번호 : {self.phone_number}\n' \
        f'이메일 : {self.e_mail}\n' \
        f'주소 : {self.addr}\n' \
        '====================================='
        return res_str
    
    def isNameExist(self, name) -> bool:
        if self.name == name :
            return True
        else :
            return False

dir_name = 'C:/Repository/StudyPython_Kasan/Day4/' #절대경로 #읽기, 저장에 한줄씩 적힐거 위로 빼서 쉽게 불러오기 편하게 위로 뺌

# 파일 저장함수
def saveContacts(contacts):
    global dir_name
    f = open(f'{dir_name}contacts.txt', mode='w', encoding='utf-8')  ## mode = 'w' write 쓴다
    for item in contacts:
        f.write(f'{item.name}/{item.phone_number}/{item.e_mail}/{item.addr}\n')

    f.close()

# 파일 로드함수(읽기)
def loadContacts(contacts):
    global dir_name
    f = open(f'{dir_name}contacts.txt', mode='r', encoding='utf-8')  ## mode = 'r' read 읽는다 
    while True:
        line = f.readline()
        if not line: 
            break

        lines = line.replace('\n','').split('/') # 탈출문자 (\n \r) 전부 삭제** 
        contact = Contact(lines[0],lines[1],lines[2],lines[3])
        contacts.append(contact)

    f.close()  #파일 닫기(필수!)

# 화면 클리어 함수
def clearConsole() :
    command = 'clear' # UNIX, LINUX, MACOS
    if os.name in ('nt', 'dos') :
        command = 'cls'
    os.system(command)

# 사용자 정보 입력
def getContact() :
    member = None # 로컬변수 초기화
    try :
        (name, phone_number, e_mail, addr) = input('정보입력(이름, 폰번호, 이메일, 주소)[구분자 : /] > ').split('/')
        member = Contact(name, phone_number, e_mail, addr)
        # print(name, phone_number, e_mail, addr)
    except Exception as ex :
        # print(f'예외발생 : {ex}')
        print('정확하게 이름/폰번호/이메일/주소 순으로 입력해주세요.')

    return member

# 연락처 리스트 출력
def printContacts(contacts) :
    for item in contacts : # 리스트 원소 (Contact 객체)
        print(item)
             
# 연락처 삭제 함수
def delContact(contacts, name) :
    for i, item in enumerate(contacts) :
        if item.isNameExist(name) == True :
            del contacts[i]

# 연락처 검색 함수 220526 16:14 신규추가
def searchContact(contacts, name):
    isFind = False
    for i, item in enumerate(contacts) :
        if item.isNameExist(name) == True :
            isFind = True 
            print(item)
            break 

    if isFind == False:
        print('검색 정보가 없습니다')

# 연락처 수정 함수 220526 16:38 신규추가 
def editContact(contacts, name):
    contact = None #수정할 연락처 담을 변수 
    index = -1 # 찾은 리스트 인덱스 
    isFind = False

    for i, item in enumerate(contacts) :
        if item.isNameExist(name) == True :
            isFind = True 
            contact = item
            index = i
            break 

    if isFind == False:
        print('검색 정보가 없습니다')
    else:
        #pass # Contact객체를 보여주고 값을 수정할 입력받기 
        print('검색정보')
        print(f'{contact.name}{contact.phone_number}/{contact.e_mail}/{contact.addr}')

    try:
        # 수정할 폰번호/이메일/주소입력 
        (phone_number,e_mail,addr) = \
            input('정보입력(폰번호,이메일,주소)[구분자 : / ] > ').split('/')
        member = Contact(contact.name, phone_number, e_mail, addr)

        contacts[index] = member # 이전값을 새 연락처로 변경
    except:
            print('정확하게 이름/폰번호/이메일/주소 순으로 입력해주세요.')
    
# 메뉴 출력
def getMenu() :
    str_menu = ('주소록 프로그램 v1.2\n'
                '1. 연락처 추가\n'
                '2. 연락처 출력\n'
                '3. 연락처 검색\n'  # 22.05.26 검색기능 추가 
                '4. 연락처 수정\n'  # 22.05.26 수정기능 추가
                '5. 연락처 삭제\n'
                '6. 프로그램 종료\n')
    print(str_menu)

    menu = input('메뉴 선택 > ')
    try :
        menu = int(menu)
    except :
        menu = 0
    return menu

# 기본 실행 함수 
def run() :
    contacts = [] # 빈 리스트 변수 초기화
    try:   # 처음엔 contacts가 없어 그래서 load에서 에러가 떠 이 에러를 막고자 try 함수를 사용하고 except pass 로 contacts가 없어도 
           #프로그램이 실행될 수 있도록 4줄을 추가해 주었다 
        loadContacts(contacts)
    except:
        pass

    clearConsole()
    while True :
        sel_menu = getMenu()
        if sel_menu == 1 : # 연락처 추가
            clearConsole()
            member = getContact()
            if member != None :
                contacts.append(member)  # 연락처 리스트에 새 연락처 추가
            input('계속하려면 아무키나 누르세요. > ')
            clearConsole()
        elif sel_menu == 2 : #연락처 출력
            clearConsole()
            printContacts(contacts)
            print(f'총 {len(contacts)} 건 입니다.\n')
            print('=====================================')  
            input('계속하려면 아무키나 누르세요. > ')
            clearConsole()
        elif sel_menu ==3 : # 연락처 검색 
            clearConsole()
            name = input('검색할 이름 입력 > ')
            #검색 기능 추가
            searchContact(contacts, name)
            input('계속하려면 아무키나 누르세요. > ')
            clearConsole()
        elif sel_menu ==4 : # 연락처 수정 
            clearConsole()
            name = input('수정할 이름 입력 > ')
            #수정 기능 추가
            editContact(contacts, name)
            input('계속하려면 아무키나 누르세요. > ')
            clearConsole()

        elif sel_menu == 5 :  #연락처 삭제
            clearConsole()
            name = input('삭제할 이름 입력 > ')
            delContact(contacts,name)
            input('계속하려면 아무키나 누르세요. > ')
            clearConsole()
        elif sel_menu == 6 : # 프로그램 종료
            saveContacts(contacts) # v파일DB에 저장 
            break
        else :
            clearConsole()

if __name__ == '__main__' : #EntryPoint (프로그램 시작점)
    print('프로그램 시작') ## 프로그램이 시작됨
    try :
        run()
    except KeyboardInterrupt as ex :
        print('비정상 종료!')