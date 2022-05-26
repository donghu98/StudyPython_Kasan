'''
주소록 프로그램 v1.0
작성일 2022-05-26 09:14
작성자 쩔받은로또
설명 주소록 프로그램 테스트
''' 
import os # 운영체제 명령용 모듈
# 주소록 클래스
class Contact :
    name = ''; phone_number = ''; e_mail = ''; addr = ''

    # 생성자(constructor) 
    def __init__(self, name, phone_number, e_mail, addr) -> None:
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr
    
    def __str__(self) -> str:
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
        print('정확한게 이름/폰번호/이메일/주소 순으로 입력해주세요.')

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

# 메뉴 출력
def getMenu() :
    str_menu = ('주소록 프로그램 v1.0\n'
                '1. 연락처 추가\n'
                '2. 연락처 출력\n'
                '3. 연락처 삭제\n'
                '4. 프로그램 종료\n')
    print(str_menu)
    menu = input('메뉴 선택 > ')
    try :
        menu = int(menu)
    except :
        menu = 0
    return menu

def run() :
    contacts = [] # 빈 리스트 변수 초기화
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
        elif sel_menu == 2 : # 연락처 출력
            clearConsole()
            printContacts(contacts)
            print(f'총 {len(contacts)} 건 입니다.\n')
            print('=====================================')  
            input('계속하려면 아무키나 누르세요. > ')
            clearConsole()
        elif sel_menu == 3 :
            clearConsole()
            name = input('삭제할 이름 입력 > ')
            delContact(contacts,name)
            input('계속하려면 아무키나 누르세요. > ')
            clearConsole()
        elif sel_menu == 4 : # 프로그램 종료
            break
        else :
            clearConsole()

if __name__ == '__main__' : #EntryPoint (프로그램 시작점)
    print('프로그램 시작') ## 프로그램이 시작됨
    try :
        run()
    except KeyboardInterrupt as ex :
        print('비정상 종료!')