# if문장
# 조건문
# 주어진 조건이 참인 경우에 실행
print('if')

# 조건에는 비교연산자
# >=, <=, ==, !=
# 참 True / 거짓 False

if True:
  print('True')
  
# 자바와는 다르게 코드블럭대신 :과 탭(들여쓰기)이 이용됩니다.
res = False
if res:
  print('참인 경우에만 실행 됩니다!')
  # 부정연산자 not(! 대신 not을 사용)
elif not False:
  print("조건이 여러개인 경우")
else:
  print('거짓인 겨우에만 실행 됩니다!')
