# 실습1. 자판기의 거스름돈 구하기

# 조건
# 조건1. 물건값은 100원 단위
# 조건2. 자판기는 동전 500원, 100원만 가지고 있음
# 실습
# 물건의 가격과 지불한 금액을 입력 받고 거스름돈을 알려주는 계산대 프로그램을 작성
# 변수
# money : 투입한 금액을 저장
# price : 물건 가격을 저장
# change : 거스름돈을 저장
# coin500 : 500원 짜리 동전의 개수
# coin100 : 100원 짜리 동전의 개수
# [1000, 2000, 3000]
# 자판기 메뉴를 출력
# 사용자가 메뉴를 입력
# 가격을 빼서 잔돈을 출력
coin500 = 0
coin100 = 0

while True:
  money = int(input("얼마를 내시겠습니까?"))
  price = int(input("물건의 금액은 얼마입니까?"))

  if money < price:
    print('지불할 금액보다 물건값이 비쌉니다. 다시입력하세요.')
  else:
    real_change = change = money - price
    print(f'거스름돈은 {change}원 입니다.')
    while change >= 500:
      change -= 500
      coin500 += 1
    while change >= 100:
      change -= 100
      coin100 += 1
  print(f'500원 : {coin500}\n100원 : {coin100}')
  
  if coin500*500+coin100*100>=1000:
    price = [1000,2000,3000]
    print("""
1. 1000원
2. 2000원
3. 3000원
""")
    price_no = int(input("추가 구매하실 품목을 선택하세요.")) - 1
    print(price[price_no],"을 선택하셨습니다.")
    
    if real_change < price[price_no]:
      print('지불할 금액보다 물건값이 비쌉니다. 다시입력하세요.')
    else:
      change = real_change - price[price_no]
      print(f'거스름돈은 {change}원 입니다.')
      coin500 = coin100 = 0
      while change >= 500:
        change -= 500
        coin500 += 1
      while change >= 100:
        change -= 100
        coin100 += 1
    print(f'500원 : {coin500}\n100원 : {coin100}')
    
    break
  
print('='*50)
# 리스트를 출력시 인덱스를 사용하는 방법
items = ['포테이토칩', '계란과자', '땅콩스낵', '빼빼로']
prices = [2000, 3000, 4000, 5000]
for item in items:
  print(item)
  
for index, item in enumerate(items):
  print(f'{index}:{item}')
  
  
# 자판기에 물품을 초기화
items = ['오징어칩','포키','포테이토칩','초코파이']
prices = [2000, 1300, 1800, 1000]

# 인덱스 값을 꺼내오기 위해서 enumerate함수를 이용
for index, item in enumerate(items):
  print(f'{index}:{item}')
  

# 판매할 물건의 금액
# 100원 단위로 입력 받아요
# 문자, 실수가 입력된 경우 오류
menu = int(input('구매하실 물품을 선택해주세요'))
price = prices[menu]

print(f'선택하신 물품의 금액은 {price} 입니다.')
# 사용자로 부터 받은 금액
money = int(input("입금 : "))

# 거스름돈
change = money - price
# 문자타입 + 숫자타입 = 오류
print("거스름돈 : ",change)
print(f'거스름돈 : {change}')

# 500원의 갯수
# /실수가 반환 될 수 있다
# // 정수타입으로 반환
coin500_cnt = change//500

# 500원 거슬러주고 남은 돈
change = change % 500

# 100원의 갯수
coin100_cnt = change//100

print(f'500원 : {coin500_cnt}개, 100원 : {coin100_cnt}개')