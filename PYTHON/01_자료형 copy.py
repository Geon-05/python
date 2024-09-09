# 리스트를 만들고 1부터 5까지 입력 해보세요
# 5개의 음식을 입력받고 리스트에 추가 해보세요
# 리스트에 담겨있는 음식목록을 출력 해봅시다 - for
# 중복된 경우 입력되지 않도록 처리 - while-break
# 정렬 후 출력
# 오름차순 정렬 : sort(), 내림차순정렬 : sort(reverse=True)
# 리스트에 오렌지가 있으면 '저도 오렌지를 좋아해요' 메세지를 출력
# 리스트에 오렌지가 없으면 오렌지를 리스트에 추가

food = []
for i in range(0,5):
    insert_food = input("등록할 음식을 작성하세요.")
    print(f'{i+1}번째 등록한 음식은 {insert_food}입니다.')
    food.append(insert_food)
    print("i :",i)
    for j in range(0,i):
        print("j :",j)
        print(insert_food)
        if(insert_food == food[j]):
            print(f"{insert_food}는 이미 등록된 음식입니다.")
            food[i] = input("다시입력하세요.")
            j=0
        print(food)

print('='*50)

food = []

while True :
    in_food = input("좋아하는 음식?")
    
    if in_food in food:
        print("중복되는 음식입니다.")
        continue
    
    food.append(in_food)
    
    if len(food) >= 5 :
        break

food.sort()
print(food)