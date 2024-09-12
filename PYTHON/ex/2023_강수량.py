import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# 강수량 파일을 읽어서 모두 출력 해봅시다.
x=[]
y=[]

# 파일이 없는 경우 오류 발생
f = open('PYTHON/ex/2023_강수량.csv','r',encoding='utf-8')

while True:
    # 더이상 읽을 것이 없으면 빈문자열을 반환
    line = f.readline()
    print(line)
        
    # 빈값은 false를 반환
    if not line : break
    
    # 전개문법을 사용 할 경우
    # 값의 갯수가 맞지 않으면 오류가 발생 할 수 있다
    # 빈 값이 반환되면 반복문을 종료 하도록 처리
    a ,b, c = line.split(',')
    x.append(a[-2:])
    y.append(c.replace("\n",""))
    
    print(f'{a},{b},{c}')

print("x :",x)
print("y :",y)
print("종료")
f.close()

realX=[]
realY=[]

for t in x[1:]:
    realX.append(float(t))
    
for t in y[1:]:
    realY.append(float(t))


# 데이터 설정, 점 모양, 선 모양, 선 색
plt.plot(x, y, marker='o', color = 'blue')

# 제목
plt.title("2023년 월별 강수량")
# 축제목
plt.xlabel("월")
plt.ylabel("강수량(mm)")
# 범례
plt.legend(['2023'])

# 차트 보여줘
plt.show()