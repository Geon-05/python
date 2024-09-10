# 함수 정의
# def 함수이름(매개변수,매개변수, ...)
# a, b : 매개변수
# 매개변수의 기본값을 줄 수 있다.
# 기본값이 없는 매개변수가 앞에 와야한다!
# def add(a=0,b) : 에러발생!
# 단, 모든 매개변수에 기본값이 있는것은 괜찮다!
# def add(a=0,b=0) : 에러X
def add(a, b):
    # 매개변수 값을 확인
    print(f"a : {a}")
    print(f"b : {b}")
    # 반환타입
    return a + b


# 함수를 호출
# 2, 3 : 인수
# 인수, 파라메터 : 함수를 호출 할 때 전달하는 입력값
print(add(2, 3))
print("=" * 20)

# 매개변수 이름으로 값을 넣어 줄 수 있다.
print(add(b=2, a=3))


def print_title():
    print("=" * 5, "환영합니다.", "=" * 5)


# 함수를 호출
print_title()
# 반환이 없는 함수는 None을 반환
print("반환타입이 없는 함수의 실행 결과 : ", print_title())
# 반환이 있는 함수는 반환값을 반환
print(add(2, 3))

print("=" * 20)


# 매개변수의 갯수를 모를때는 변수명 앞에 *을 붙여 주면
# 매개변수를 튜플타입으로 받아 온다
def add(*arr):
    print("arr : ", arr)
    print("type(arr) : ", type(arr))

    sum = 0

    for num in arr:
        # sum = sum + num
        sum += num

    return sum


sum = add(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
print("sum : ", sum)

# 2개의 수와 하나의 연산자를 입력 받아서
# 연산 후 반환하는 함수를 작성 하시오.
# -,/,% 연산시 두 수중 큰 수가 앞쪽에 나오도록!


def call(num1, num2, op):
    if num1 < num2:
        num3 = num2
        num2 = num1
        num1 = num3

    print("큰수는 :", num1)
    print("작은수는 :", num2)

    if op == "+":
        print("num1 + num2 =", num1 + num2)
        return num1 + num2
    if op == "-":
        print("num1 - num2 =", num1 - num2)
        return num1 - num2
    if op == "*":
        print("num1 * num2 =", num1 * num2)
        return num1 * num2
    if op == "/":
        print("num1 / num2 =", num1 / num2)
        return num1 / num2
    if op == "%":
        print("num1 % num2 =", num1 % num2)
        return num1 % num2


call(5, 2, "+")
call(5, 2, "-")
call(5, 2, "*")
call(5, 2, "/")
call(5, 2, "%")
