from datetime import datetime

# hello() : '어서오세요'를 출력 하는 함수
# hello(name) : '00님 환영합니다.'를 출력하는 함수
def hello():
    print("어서오세요")

hello()

def hello(name):
    print(f"{name}님 환영 합니다.")

# hello()오류
hello("김민수")

def hello(name, age):
    print(f"{name}님({age}) 환영 합니다.")

# hello()오류
hello("김민수", 13)
# 매개변수의 이름으로 값을 넣는 방법
hello(age=13, name="박서현")

print("="*30)
# gugudan(dan) : 단에 해당하는 구구단을 출력
def gugudan(dan) :
    for i in range(1,10):
        print(f'{dan} * {i} = {dan * i}')

gugudan(3)

print("="*30)
# add(a,b) : 두 수의 합을 반환하는 함수
def add(a,b):
    return a + b

print(add(1,3))
print(f"add(10, 10) : {add(10, 10)}")

print("="*30)
# 함수 만들기
# 주민등록번호를 입력받아서 성별을 반환하는 함수
name, age = ['박서현', 13]
def getGneder(ssn):
    ssn = str(ssn)
    ssn.replace('-','')
    if not ssn.isnumeric:
        print("숫자만 입력 가능 합니다.")
        return
    if len(ssn) != 13:
        print("주민등록 번호는 13자리로 입력 해주세요.")
        return
        
    # 유효성 검증
    # 1111114444444 : 13자리 숫자
    # 오류가 발생하지 않도록 문자로 형변환
    if ssn[6] not in ['1','2','3','4']:
        print("주민번호 형식에 일치 하지 않습니다.")
        return
    if ssn[6] in ['1','3']:
        return "남"
    if ssn[6] in ['2','4']:
        return "여"

print('성별 :',getGneder('1111112222222'))
print('성별 :',getGneder(1111112222222))
print('성별 :',getGneder(111111))
# 주민등록번호를 입력받아서 나이를 반환하는 함수
def getAge(ssn) :
    res = 0
    yyyy = datetime.now().year
    yy = ssn[:2]
    if ssn[6] in ['1', '2']:
        yy = '19' + yy
    if ssn[6] in ['3', '4']:
        yy = '20' + yy
    else :
        print('주민등록 번호 형식에 맞지 않습니다.')
        return res
    print("올해 년도 :", yyyy)
    print("태어난 년도 :", yy)
    res = yyyy - int(yy)
    print('나이 :',age)
    return res


# 이름과, 주민등록번호를 입력받아서 이름, 성별, 나이를 반환하는 함수
# getGender()
def getInfo(name, ssn) :
    # 이름, 나이, 주민번호를 반환
    name = name
    # 함수를 호출 하여 나이와 성별을 반환 받아 변수에 저장
    age = getAge(ssn)
    gender = getGneder(ssn)
    
    info = [name, age, gender]
    return info

a, b, c = getInfo('박서현','1111113333333')

print(f'이름 : {a}, 나이 : {b}, 성별 : {c}')

print("="*30)
# 계산기 - 입력이 잘못된 경우 0을 반환
def cacl(operator, num1, num2) :
    # operator : +-*/%
    if operator not in ['+', '-', '*', '/', '%']:
        return 0
    # .isnumeric() : 문자열이 가지고 있는 함수
    # 문자열인 경우에만 사용이 가능
    # 타입이 다른 경우 사용 할 수없음
    # 'int' object has no attribute 'isnumeric'
    # 함수에 괄호를 붙이지 않았을 때
    # <built-in method isnumeric of str object at 0x0000029761B8C7B0>
    print('='*10,str(num1).isnumeric)
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "%":
        return num1 % num2

print('cacl("+",10,100)',cacl('+',10,100))

# 리스트, 튜플, 딕셔너리, set
# bool()
# datetime
# random
# 함수(def, 매개변수, 반환)




print("="*30)
# 함수를 만들어 봅시다
# 함수명 : calc(operator, *args)
# operator : 연산자
# args : 숫자가 저장된 튜플
# *을 사용하면 튜플로 값을 받아온다
# 매개변수를 넣지 않으면 빈 튜플로 처리된다.
def calc(operator, *args):
    res = 0
    # operator : +-*/%
    if operator not in ['+','-','*','/','%']:
        print("연산자를 확인하세요.")
        return res
    elif len(args) < 2:
        print('수를 2개 이상 입력 해주세요.')
        return res
    
    print(sorted(args, reverse=True))
    for num in args :
        res += num
        
    return res


print(calc('+',))
print(calc('+',2,1))


# 평균을 구해 봅시다.
def avg(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    avgNo = sum / len(numbers)
    
    return avgNo

print(avg(1,3,5))