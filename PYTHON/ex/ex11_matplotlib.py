# 맷플롯립(matplotlib)
# 복잡한 자료는 숫자나 텍스트 보다 그래프나 차트로 
# 데이터를 시각화 하여 이해하고 분석 하는 것이 효과적입니다

# mat   : 매트랩이라는 유명한 수치해석및 데이터 시각화 프로그램
# plot  : 그래프 그리기
# lib   : 라이브러리
# 파이썬에서 그래프 차트 등으로 데이터를 시각화 하는데 편리한 라이브러리 

# pip 환경변수를 설정
# -> 어느경로에서든지 명령어를 실행 할 수 있도록 하는 작업
# 업데이트가 필요한 경우도 있음
# cmd창을 열고 명령어를 실행
# 파이썬이 실행된다음 명령어를 실행하면 작동되지 않음 - 파이썬으로 작동되어 작동이안됨
# 설치
# pip install matplotlib
# 설치확인
# pip list

# 간단한 그래프 그리기
import matplotlib.pyplot as plt

# 한글깨짐 해결
# 맷플롭에서 사용하는 폰트를 한글폰트로 변경
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)


# fig, ax = plt.subplots()

# 축의 값을 세팅
x = [1, 2, 3, 4, 5]
y1 = [1, 2, 3, 4, 10]
y2 = [0, 5, 6, 10, 5]
y3 = [2, 3, 4, 5, 6]

# color : 선의 색상
# linestyle : 선의 모양
# marker : 마커모양
# 그래프 추가
plt.plot(x, y1, marker='x', color = 'red', linestyle='--')
plt.plot(x, y2, marker='o', color = 'blue')
plt.plot(x, y3, marker='o', color = 'green')

# 제목
plt.title("나의 첫 그래프")
# 축제목
plt.xlabel("x축")
plt.ylabel("y축")
# 범례
plt.legend(['그래프1','그래프2','그래프3'])

plt.show()