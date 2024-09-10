from datetime import datetime

# hello() : '어서오세요'를 출력 하는 함수
# hello(name) : '00님 환영합니다.'를 출력하는 함수
def hello(name=None):
    if name == None:
        print("어서오세요")
    else:
        print(f"{name}님 환영합니다.")

hello()
hello("김민수")

print("="*30)
# gugudan(dan) : 단에 해당하는 구구단을 출력
def gugudan(dan) :
    print(f"구구단 출력기 {dan}단을 출력합니다.")
    for i in range(1,10):
        print(f"{dan} * {i} = {dan*i}")

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
# getGender()
def getGender():
    idNo = input("주민등록번호를 입력하세요.").replace(" ","").replace("-","")
    if idNo[6] in ["1", "3"]:
        return "남성"
    elif idNo[6] in ["2", "4"]:
        return "여성"
    else:
        print("잘못된 번호입니다.")

print(getGender())

print("="*30)
# 주민등록번호를 입력받아서 나이를 반환하는 함수
def getGender():
    idNo = input("주민등록번호를 입력하세요.").replace(" ","").replace("-","")
    if idNo[6] in ["1", "2"]:
        return 2024 - int("19"+idNo[:2])
    elif idNo[6] in ["3", "4"]:
        return 2024 - int("20"+idNo[:2])
    else:
        print("잘못된 번호입니다.")

print(getGender())

print("="*30)
# 이름과 주민등록번호를 입력받아서 이름, 성별, 나이를 반환하는 함수
def getGender():
    info = {}
    info['name'] = input("이름을 입력하세요.")
    idNo = input("주민등록번호를 입력하세요.").replace(" ","").replace("-","")
    if idNo[6] in ["1", "3"]:
        info['gender'] = "남성"
    elif idNo[6] in ["2", "4"]:
        info['gender'] = "여성"
        
    if idNo[6] in ["1", "2"]:
        info['age'] = datetime.now().year - int("19"+idNo[:2])
    elif idNo[6] in ["3", "4"]:
        info['age'] = datetime.now().year - int("20"+idNo[:2])
    else:
        print("잘못된 번호입니다.")
    
    return info

info = getGender()

print(f"{info['name']}님의 성별은 {info['gender']}이고 나이는 {info['age']}입니다.")

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
    
    numList = sorted(args, reverse=True)
    i = 0
    if operator == "+":
        print("더하기")
        while len(numList) > i+1:
            numList[0] += numList[i+1]
            i += 1
        return numList[0]
    if operator == "-":
        print("빼기")
        while len(numList) > i+1:
            numList[0] -= numList[i+1]
            i += 1
        return numList[0]
    if operator == "*":
        print("곱하기")
        while len(numList) > i+1:
            numList[0] *= numList[i+1]
            i += 1
        return numList[0]
    if operator == "/":
        print("나누기")
        while len(numList) > i+1:
            numList[0] /= numList[i+1]
            i += 1
        return numList[0]
    if operator == "%":
        print("나머지")
        while len(numList) > i+1:
            numList[0] %= numList[i+1]
            i += 1
        return numList[0]
    

print(calc('+',))
print(calc('+',1,2,3,4))
print(calc('-',1,2,3,4))
print(calc('*',1,2,3,4))
print(calc('/',1,2,3,4))
print(calc('%',1,2,3,4))