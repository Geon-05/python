# 주민번호를 반복해서 입력 받으세요
# 사용자의 입력값에 있는 공백과 - 는 제거
# 유효성 검증
# 1. 13자리
# 2. 숫자변환가능
# 3. 7번째 자리가 1,2,3,4중 하나인지
# 유효성검증 실패시 반복문을 탈출
program = True
yyyy = 2024

while program:
    id_no = (input("주민등록 번호(13자리)를 입력하세요.").strip().replace("-", "").replace(" ", ""))

    if len(id_no) == 13:
        if int(id_no[6]) in [1, 2, 3, 4]:
            if int(id_no[6]) in [1, 3]:
                print("남성입니다.")
                if int(id_no[6]) == 1:
                    yy = "19" + id_no[:2]
                    age = yyyy - int(yy)
                    print(f"나이는 {age}입니다.")
                elif int(id_no[6]) == 3:
                    yy = "20" + id_no[:2]
                    age = yyyy - int(yy)
                    print(f"나이는 {age}입니다.")
            elif int(id_no[6]) in [2, 4]:
                print("여성입니다.")
                if int(id_no[6]) == 2:
                    yy = "19" + id_no[:2]
                    age = yyyy - int(yy)
                    print(f"나이는 {age}입니다.")
                elif int(id_no[6]) == 4:
                    yy = "20" + id_no[:2]
                    age = yyyy - int(yy)
                    print(f"나이는 {age}입니다.")
        else:
            print("주민번호 뒷자리 첫번째는 1,2,3,4만 입력가능합니다.")
            print("프로그램을 종료합니다.")
            program = False
    else:
        print("주민등록 번호는 숫자13자리로만 입력해주세요.")
        print("프로그램을 종료합니다.")
        program = False

    while True:
        res = input("프로그램을 종료합니까?(y/n)").lower()

        if res == "y":
            exit()
        elif res == "n":
            break
        else:
            print("잘못입력하셨습니다.")
