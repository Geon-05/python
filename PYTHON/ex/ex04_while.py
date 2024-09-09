# 1~100까지 수의 합 출력
i = 1
sum = 0

while i <= 100:
  sum += i
  i += 1
  
print(sum)


print("="*50)
# 1~100까지 수 중 홀수의 합만 출력

i = 1
sum = 0

while i <=100 :
  if i % 2 == 1:
    sum += i
  
  i += 1
  
print(sum)