# 키워드 매개변수
# 매개변수에 *을 붙일때
# * : 튜플로 받아옴
# ** : 딕셔너리로 받아옴
# -> 키-값 으로 저장되므로 변수의 이름이 지정되어 있어야 함

def print_kwargs(**kwargs):
    print(kwargs)

# 키워드 매개변수를 호출 할 때는 변수명을 지정 해야 한다
# 지정하지 않으면 오류
# print_kwargs(1) -> TypeError: print_kwargs() takes 0 positional arguments but 1 was given
print_kwargs(a=1)
print_kwargs(age=13, name="김지혜")

def print_kwargs(**kwargs):
    print(kwargs)
    return '첫번째 반환'
    return '두번째 반환'

print(print_kwargs())

# 매개변수에 초기값 지정하기
# 초기값이 지정된 매개변수는 뒤쪽에 위치 해야 함!
# 기본값이 없는 매개변수가 앞쪽에 위치!

def say_myself(name, age, man=True) :
    print(name)
    print(age)
    if man :
        print("남자")
    else:
        print("여자")

# 값을 넣지 않았을때 초기값이 실행
say_myself("김지훈",50,)
say_myself("김지훈",50)
say_myself("김지혜",20,False)

# 함수 안에서 선언한 변수의 유효범위
# 함수 밖에서 선언한 변수를 함수에서 사용하는 방법
var1 = '함수밖변수1'
var2 = '함수밖변수2'
var3 = '함수밖변수3'
var4 = '함수밖변수4'

def varTest(var1):
    # 함수안에서만 사용되는 변수
    print("var1 :",var1)
    # 외부에 있는 변수에 접근이 가능 하나
    var2 = '123'
    print("var2 :",var2)
    # 외부에 있는 변수명과 동일한 이름으로 사용 하려면
    # 값을 할당 하고 사용 할 수 있음
    print("var2 :",var2)
    # 함수안의 새로운 변수가 생성
    var3 = '외부변수 변경'
    print("함수안에서 출력한 var3",var3)
    
    # 전역변수에 접근해서 값을 변경 하기 위해서 global 키워드를 사용
    global var4
    var4 = '함수 안에서 변경'
    print("var4 :",var4)

# varTest() -> 매개변수를 넣지 않아 오류 - TypeError: varTest() missing 1 required positional argument: 'var1'
# 초기화 값이 있는 경우, 값을 여러개 받는 경우에만 생략이 가능
varTest(var1)
print(var2,"체크체크!!!!!!!!!!!!!!!!1")
varTest("함수의 인수")
print("함수안에서 출력한 var3",var3)
print("var4 :",var4)

# ✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨
# 전역변수
var1 = '함수밖 변수'
var2 = '함수밖 변수'

# 변수명 = 값
def verTest(var1=var1) :
    # 전역변수를 함수에서 사용
    global var2
    print(var1)
    # 그냥 외부에있는 변수에 접근하는것은 가능함
    # 하지만 외부에 있는 변수를 접근후 값 변경은 불가능함.
    # 지역변수로 정의
    var2 = '함수안에서 변경'
    var1 = '바보'
    print(var2)
    print(var1)
    
verTest()

# ✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨

# 리스트 생성
a = [1,2,3]
# 주소값이 들어감
b = a
a.append(4)
# a,b는 같은 주소를 바라보고 있으므로
# 리스트가 변경되면 같이 변경
print('a :',a)
print('b :',b)

a = '안녕'
b = a
b = '변경'
print(a)
print(b)

test_var = "테스트"
def varTest2(test_var=test_var):
    print("test_var1 :",test_var)
    
    test_var = "변경"
varTest2()
print("test_var2 :",test_var)

def add(a, b):
    return a + b

print(add(1,2))

# 익명의 함수를 변수에 저장 하여 사용 할 수 있다.
# lambda 매개변수, .. : 반환값
add1 = lambda a, b : a + b
print(add1(1,2))

# 리스트의 컴프리핸션
# 반복이 가능한 객체를 대상으로 새로운 객체를 만들어 내는 것

a = [1, 2, 3, 4, 5]
res = []
# 기존 리스트의 요소 값에 3을 곱한 새로운 리스트를 만들고 싶다.
for i in a:
    res.append(i*3)
print(a)
print(res)
# [반환값 for 변수명 in 반복할대상 if 조건]
res = []
res = [i*3 for i in a if i % 2 == 0]
print(res)