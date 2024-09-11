import math

def gugu(dan):
    gugu_res = []
    i = 1
    while True:
        gugu_res.append(dan*i)
        i += 1
        if i > 9:
            break
    return gugu_res

print(f'2단{gugu(2)}')

def ex02():
    res = 0
    i = 1
    while True:
        if i % 3 == 0 or i % 5 == 0:
            res += i
        i += 1
        if i>=1000:
            break
    print(res)
    
ex02()

def get_total_page(m, n):
    page = math.ceil(m/n)
    return page

print(get_total_page(4,5))
print(get_total_page(10,5))
print(get_total_page(11,5))