import csv
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

year = 2018
colors = ['blue','green','red','yellow','black','cyan']
years = []

while True:
    f = open(f'PYTHON/ex/csv/{year}_강수량.csv','r',encoding='utf-8')
    # csv.reader : 구분자로 끊어서 리스트에 담아서 반환
    csvfile = csv.reader(f, delimiter=',')

    # 제목읽어오기
    header = next(csvfile)

    x = []
    y = []

    for line in csvfile :
        x.append(float(line[0][-2:]))
        y.append(float(line[2]))
    
    plt.plot(x, y, marker='o', color = colors[year-2018])
    years.append(str(year)+"년")
    
    year += 1
    
    if year > 2023:
        break

# 데이터 설정, 점 모양, 선 모양, 선 색

# 제목
plt.title("월별 강수량")
# 축제목
plt.xlabel("월")
plt.ylabel("강수량(mm)")
# 범례
plt.legend(years)

# 차트 보여줘
plt.show()