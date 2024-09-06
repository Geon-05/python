# 학생의 이름과 국어, 영어, 수학 성적을 입력받고
# 3개의 성적을 입력 받아서 평균을 구하고 평균점수가
# 90점 이상 : A학점
# 80점 이상 : B학점
# 70점 이상 : C학점
# 60점 이상 : D학점
# 학점과 이름을 출력하세요

name = input("이름 :")
korean = float(input("국어 성적을 입력하세요."))
english = float(input("영어 성적을 입력하세요."))
math = float(input("수학 성적을 입력하세요."))

evg = (korean+english+math)/3

if evg >= 90:
  score = "A"
elif evg >= 80:
  score = "B"
elif evg >= 70:
  score = "C"
elif evg >= 60:
  score = "D"
else:
  score = "F"
  
print('%s님의 성적은 %s학점 입니다.' %(name, score))