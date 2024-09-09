import random

# 임의의 수를 추출
# 0부터 끝값까지 (시작값 0, 끝값은 포함되지 않음)
# random.randrange(끝값)

# 0,1
num = random.randrange(2)
print(num)

# 0 ~ 9
num = random.randrange(10)
print(num)

# 5 ~ 9
num = random.randrange(5, 10)
print(num)

print("=" * 50)

num = ""
for i in range(6):
    num += str(random.randrange(36)) + ", "
    print(num)
