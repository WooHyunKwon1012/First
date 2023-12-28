import math
def sqt(a):
    b=pow(a,2)
    return b

a=int(input("숫자를 입력하시오 : "))
print(sqt(a))

def circle_area(a):
    b=a*a*3.14
    return b
r=int(input("반지름을 입력하세요 : "))
print(circle_area(r))

def sub(a, b):
    return a - b

result = sub(a=7, b=3)
print(result)
result = sub(b=5, a=3)
print(result)
result=sub(1,2)
print(result)

