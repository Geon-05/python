# 학생의 이름과 국어, 영어, 수학 성적을 입력받고
# 3개의 성적을 입력 받아서 평균을 구하고 평균점수가
# 90점 이상 : A학점
# 80점 이상 : B학점
# 70점 이상 : C학점
# 60점 이상 : D학점
# 학점과 이름을 출력하세요

name = input("이름 :")
score1 = int(input("국어점수 :"))
score2 = int(input("영어점수 :"))
score3 = int(input("수학점수 :"))

# // : 나눗셈 후 정수를 반환
avg = (score1 + score2 + score3) / 3

print(name, "학생의 평균점수는", avg, "입니다.")
print("%s학생의 평균점수는 %.2f입니다." % (name, avg))

if avg >= 90:
    print("A", "학점 입니다.")
elif avg >= 80:
    print("B", "학점 입니다.")
elif avg >= 70:
    print("C", "학점 입니다.")
elif avg >= 60:
    print("D", "학점 입니다.")
else:
    print("재수강 하셔야 합니다.")

# ✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨


name = input("이름 :")
korean = float(input("국어 성적을 입력하세요."))
english = float(input("영어 성적을 입력하세요."))
math = float(input("수학 성적을 입력하세요."))

avg = (korean + english + math) / 3

if avg >= 90:
    score = "A"
elif avg >= 80:
    score = "B"
elif avg >= 70:
    score = "C"
elif avg >= 60:
    score = "D"
else:
    score = "F"

print("%s님의 성적은 %s학점 입니다." % (name, score))
