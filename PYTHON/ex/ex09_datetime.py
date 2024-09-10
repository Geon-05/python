from datetime import datetime, timedelta

# 사용자의 입력일로 부터 7일 후 날짜를 출력
input_day = input("대여일(yyyy-mm-dd) : ")
# datetime(년,월,일)
list_day = input_day.split('-')
day = datetime(int(list_day[0]),int(list_day[1]),int(list_day[2]))

returnDay = day + timedelta(days=7)
print(returnDay)
print(returnDay.strftime("%Y-%m-%d(%a)"))