import csv
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

x = [1,2,3,4]
y = [1,2,3,4]

# x축데이터, y축데이터, 마커, 선, 색상
plt.plot(x,y, marker='x', color='r')

x = [2,3,4,5]
y = [1,2,3,4]

plt.plot(x,y, marker='x', color='b')

plt.show()
