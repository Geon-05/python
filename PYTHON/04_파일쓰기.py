# f = open('새파일.txt','w')
# f.close()

# # open(파일명, 모드)
# # 쓰기모드(덮어쓰기)
# open('새파일.txt','w', encoding='utf-8')
# # 쓰기모드(이어쓰기)
# open('새파일.txt','a')
# # 읽기모드
# open('새파일.txt','r')

# # 파일을 만들고
# f = open('새파일.txt','w')
# # 파일을 닫는다!
# f.close()

# 파일출력 = 파일객체가 닫혀진 이후에는 접근 안됨
# 파일이 존재하지 않는 경우 오류 발생
f = open('새파일1.txt', 'w', encoding='utf-8')
f.write("안녕하세요\n")
f.write("반가워요\n")

for i in range(1,20) :
    f.write(f"{i}번째 줄입니다. \n")

f.close()