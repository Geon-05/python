from datetime import datetime, timedelta
import locale
import os

# 현재 날짜와 시간을 가지고 오기
now = datetime.now()

# 모듈이름에 .을 붙이면
# 모듈이 가지고 있는 함수, 변수를 사용 할 수 있다
print(now)  # 현재 시간날자
print(now.date())  # 현재 시간날자
print(now.year)  # 현재 년
print(now.month)  # 현재 월
print(now.day)  # 현재 일
print(now.hour)  # 현재 시간
print(now.minute)  # 현재 분
print(now.second)  # 현재 초
print("-"*20)
print(now.strftime("%Y-%m-%d(%a) %H:%M:%S"))

# 2024,12,25 일이 무슨 요일인지 출력 해봅시다.
day = datetime(2024,12,25)
print(day.strftime("%a"))

if os.name == 'nt':  # Windows
    locale.setlocale(locale.LC_TIME, 'kor')
else:  # Linux, Mac
    locale.setlocale(locale.LC_TIME, 'ko_KR.UTF-8')

day = datetime.now()
print(day.strftime("%a"))
day = datetime(2024,12,25)
print(day.strftime("%a"))

# 날짜연산
# timedelta
# datetime 모듈에서 제공하는 클래스
# 날짜와 시간의 연산을 간편하게 처리

# 다음날
# 함수를 호출 할 때 매개변수의 이름을 지정 하면
# 매개변수의 순서에 상관없이 값을 넣어 줄 수 있다.
nextDay = now + timedelta(days=1)
print(f'내일 : {nextDay}')

# imedelta의 매개변수
# days		: 날짜의 차이. 양수나 음수의 정수 값을 지정.
# seconds	: 초 단위의 차이. 0에서 86399 사이의 값을 지정.
# minutes	: 분 단위의 차이. 0에서 59까지의 값을 지정.
# hours		: 시간 단위의 차이. 0에서 23까지의 값을 지정.
# weeks		: 주 단위의 차이. 양수나 음수의 정수 값을 지정.
# 날짜 형식 지정
# %Y	: 연도 (예: 2024)
# %m	: 월 (01에서 12)
# %d	: 일 (01에서 31)
# %H	: 시간 (24시간 형식, 00에서 23)
# %M	: 분 (00에서 59)
# %S	: 초 (00에서 59)
# %a	: 요일의 축약형 (예: Mon, Tue, Wed)
# %A	: 요일의 전체 이름 (예: Monday, Tuesday, Wednesday)
# %b	: 월의 축약형 (예: Jan, Feb, Mar)
# %B	: 월의 전체 이름 (예: January, February, March)

# 실습3
while True:
    day_input = input('도서의 대여일(년-월-일)')
    day_list = day_input.split('-')
    day = datetime(int(day_list[0]),int(day_list[1]),int(day_list[2]))
    print(day_list)

    if day_input[4] != '-' or day_input[7] != '-':
        print("입력날짜의 형식이 올바르지 않습니다.")
        continue

    returnDay = day + timedelta(days=7)
    print(day_list)

    print(f'도서의 대여일은 {day_list[0]}년 {day_list[1]}월 {day_input[-2:]}일 입니다.')
    print(f'도서의 반납일은 {returnDay[0]}년 {returnDay[1]}월 {returnDay[2]}일 입니다.')
    
    res = input("프로그램을 종료합니까?(y)")
    
    if res.lower() == "y":
        exit()