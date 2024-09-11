# 함수정의
# 단을 입력받아서 구구단 프로그램작성
def gugu(dan):
    res = []
    print(dan)
    res.append(f'{dan}단')
    for i in range(1,10):
        res.append(dan * i)
        print(dan*i, end=', ')
    print()
    return res


# 함수 호출
res = gugu(2)
print(res)

# end값 미만의 수를 출력
# 범위를 입력 받아서 3의 배수, 5의 배수의 합을 출력
def test(end):
    # print(list(range(1,end)))
    res = 0
    for i in range(1,end):
        # 3의 배수이거나 5의 배수이면 출력
        if i % 3 == 0 or i % 5 == 0 :
            print(i)
            res += i
    return res
res = test(1000)
print(res)


# 게시판 페이징
# 게시물의 총 갯수와 한 파이지에 보여줄 게시물의 수를 입력받아서
# 총 페이지수를 반환 하는 함수
print("="*20)
def get_total_page(total_cnt, amount) :
    # total_cnt : 게시물의 총 건수
    # amount : 한 페이지에 보여질 게시물의 수
    # // : 정수를 반환
    # 나머지가 있다는건 더 보여줄 게시물이 있다는 의미
    # 나머지가 없다는건 다음 페이지가 없다는 것과 같음
    if total_cnt % amount == 0:
        return total_cnt//amount
    else : 
        return total_cnt//amount + 1

import math
def get_total_page1(total_cnt, amount):
    return math.ceil(total_cnt/amount)

print(get_total_page(5,10))
print(get_total_page(15,10))
print(get_total_page(25,10))
print(get_total_page(30,10))
print(get_total_page1(5,10))
print(get_total_page1(15,10))
print(get_total_page1(25,10))
print(get_total_page1(30,10))