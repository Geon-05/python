def ex150_03():
    i = 0
    while True :
        i += 1
        if i<=5:
            print("*"*i)
        else :
            break

ex150_03()

def ex150_05():
    A = [70,60,55,75,95,90,80,80,85,100]
    total = 0
    for score in A:
        total += score
    average = total/len(A)
    return average
    
print(ex150_05())

def ex150_06():
    numbers = [1,2,3,4,5]
    result = []
    for n in numbers:
        if n % 2 == 1:
            result.append(n*2)

def ex150_06_com():
    numbers = [1,2,3,4,5]
    result = [num * 2 for num in numbers if num % 2 ==1]
    print(result)

ex150_06_com()

def ex129():
    pocket = ['paper','money']
    if 'card' in pocket:
        print("카드가 있어요!")
        return pocket
    else:
        print("카드가 없어요! 잊지마세요!")
        pocket.append('card')
        return pocket

print(ex129())

def ex139():
    i = 1
    while True:
        if i % 3 != 0:
            print(i)
        i += 1
        if i>10:
            break

ex139()

def ex145():
    sum = 0
    for i in range(1,101):
        sum += i
    print(sum)

ex145()