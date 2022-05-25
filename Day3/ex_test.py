# 예외처리 테스트

def add(x,y):         #정의한거임
    res = x + y
    return res

def sub(x,y):
    res = x - y
    return res

def mul(x,y):
    res = x * y 
    return res

def div(x,y):    #실행/디버깅버튼 누르고 F10을 해서 어디가 예외인지 알 수가 있었다 
    res = x / y  #여기서 예외가 발생했다는 것을 알 수가 있음 
                 #shift + f5 누르면 실행/디버깅에서 벗어날 수 있음
    return res   #예외발생 ''' -> 비정상적으로 프로그램이 끝남(가끔 프로그램 에러나는 것처럼)

print('계산기 시작')
(x,y) = (4,1)
print(f'더하기 {x} + {y} = {add(x,y)}')    #21번만 실행되고 나머지는 실행X

try:
    print(f'나누기 {x} / {y} = {div(x,y)}')   
    print('17' + 3)
except ZeroDivisionError as ex:  #ZeroDivisionError 처리
    print(f'제수에 0을 넣으면 안됩니다.{ex}') 
    #pass  #비정상적인 프로그램실행을 막은 거임 try, except, pass를 통하여 
except TypeError as ex:
    print('문자열과 수를 더할 수 없습니다')
except Exception as ex:
    print(f'예외가 발생했습니다 {ex}')
#except Exception : 예외의 어머니뻘
#                  여기서 예외 다 걸림 --> 잠깐 예외를 제쳐두고 진도뺄수잇다
finally:
    print('예외가 발생한 구간을 지나갔습니다')

print(f'빼기 {x} - {y} = {sub(x,y)}')
print(f'곱하기 {x} * {y} = {mul(x,y)}')
print('계산기 종료')       #예외로 더하기만 실행되고 나머지는 실행되지 않음 -> 신뢰도떨어짐
###디버깅 완전 많이많이 중요하다!!
##디버깅 예외처리 하는 방법을 꼭 익힐것 
