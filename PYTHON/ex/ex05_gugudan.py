# 구구단
# 1. 2단부터 9단까지 출력 하시오.
for i in range(2,10):
  print(f'{i}단을 출력합니다.')
  for j in range(1,10):
    print(f'{i} * {j} = {i*j}')


# 2. 홀수단만 출력
for i in range(2,10):
  if i % 2 == 1:
    print(f'{i}단을 출력합니다.')
    for j in range(1,10):
      print(f'{i} * {j} = {i*j}')

# range() 함수를 이용해서 숫자 리스트를 만들어 반복문을 이용 합니다.
row = ''

for i in range(1,10):
  for j in range(2,10):
    row += str(j)+' * '+str(i)+" = "+str(j*i)+" / "
  row += "\n"
  
print(row)

