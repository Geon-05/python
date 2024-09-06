# 두 수를 입력 받고 두 수의 합을 출력하는 프로그램을 작성
# 출력양시 : 입력값1 + 입력값2 = 입력값1 + 입력값2

num1 = int(input('입력값1 :'))
num2 = int(input('입력값2 :'))

# 형식 출력
# %d : 정수
# %f : 실수
# %s : 문자열
print('%d + %d = %d' %(num1, num2, num1+num2))
print('%d - %d = %d' %(num1, num2, num1-num2))
print('%d * %d = %d' %(num1, num2, num1*num2))
print('%d / %d = %d' %(num1, num2, num1/num2))

# BMI구하기
# 사용자로부터 키와 몸무게를 입력 받아 BMI를 구하는 프로그램을 작성
# BMI = 몸무게/(키*키)
# 몸무게의 단위는 kg, 키의 단위는 m
# BMI의 값에 따라 문자를 출력
# 25이상 비만, 23이상 과체중, 18.5이상 정상, 나머지는 저체중

# 사용자로 부터 키와 몸무게를 입력 받아 실수 타입으로 형변환 하여 변수에 저장
# input()의 반환타입은 문자타입이므로 형변환 해야 숫자의 연산 결과를 받을 수 있다.
while True:
  msg = '''
BMI 계산기
  '''
  print(msg)
  
  height = float(input('키(m) : '))
  weight = float(input('몸무게(kg) :'))

  bmi = weight / (height*height)

  print('bmi는 ',bmi,'입니다.')

  if bmi >= 25:
    print("비만 입니다.")
  elif bmi >= 23:
    print('과체중')
  elif bmi >= 18.5:
    print('정상')
  else :
    print('저체중')
  
  next = ''
  
  while next.lower() not in ['y','n']:
    next = input("계속 하시겠습니까?")
    
  
  print('next',next)
  # print("next != 'y'",next != 'y')

# 소문자로 변환후 비교
  if next.lower() != 'y':
    print('lower : ',next.lower())
    continue # 다음 반복으로 넘어감
  else:
    break # 반복문을 탈출함
  
  # continue를 만나면 이후 블럭은 실행하지 않고 다음 반복으로 넘어가므로
  # 아래 출력문장은 실행 되지 않는다
  
  print("="*30)


# 제어문 사용시 들여쓰기를 무시하면 오류 발생!
# 조건문에는 비교연산자를 사용하거나 True, False 값을 사용
res = True
while res:
  print("여기서부터 새로운것!")
  height = float(input('키는 몇 m입니까?'))
  weight = float(input("몸무게는 몇 kg입니까?"))
  
  if height>=100:
    height = height/100

  bmi = weight/(height*height)
  print(bmi)

  if bmi >= 25:
    print("비만입니다.")
  elif bmi >=23:
    print("과체중입니다")
  elif bmi >= 18.5:
    print("정상입니다.")
  else:
    print("저체중입니다.")
  
  while True:
    in_res = input("프로그램을 종료합니까?(Y/N)")
    
    if in_res == "Y" or in_res == "y":
      res = False
      break
    elif in_res == "N" or in_res == "n":
      res = True
      break
    else:
      print("잘못입력하셨습니다.")