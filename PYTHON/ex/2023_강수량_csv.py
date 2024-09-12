import csv
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

f = open('PYTHON/ex/2023_강수량.csv','r',encoding='utf-8')
# csv.reader : 구분자로 끊어서 리스트에 담아서 반환
csvfile = csv.reader(f, delimiter=',')

# 제목읽어오기
header = next(csvfile)

x = []
y = []

for line in csvfile :
    x.append(line[0].replace('2023-',''))
    y.append(float(line[2]))

# 데이터 설정, 점 모양, 선 모양, 선 색
plt.plot(x, y, marker='o', color = 'blue')

# 제목
plt.title("2023년 월별 강수량")
# 축제목
plt.xlabel("월")
plt.ylabel("강수량(mm)")
# 범례
plt.legend(['2023년'])

# 차트 보여줘
plt.show()