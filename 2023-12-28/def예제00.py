def calc():
    a=int(input("숫자 1 입력:"))
    b=int(input("숫자 2 입력:"))
    res=a//b
    od=a%b
    print("{}를 {}로 나눈 몫은 {}이고, 나머지는 {}입니다.".format(a,b,res,od))

calc()

def calc1(a,b):
    
    res=a//b
    od=a%b
    return res,od

a=int(input("숫자 1 입력:"))
b=int(input("숫자 2 입력:"))
c,d=calc1(a,b)
print("{}를 {}로 나눈 몫은 {}이고, 나머지는 {}입니다.".format(a,b,c,d))

def cala(a,b):
    res=a//b
    que=a%b
    return res,que #이 순서에 따라 값이 리턴됨

a=int(input(":"))
b=int(input(":"))

c,d=cala(a,b) #좌우를 바꾸면 성립하지 않음
print(c,d)