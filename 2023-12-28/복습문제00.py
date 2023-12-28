fruit=dict(바나나=5, 사과=3, 체리=6)

while True:
    ord=input("구매할 과일 : ")
    if ord == "q":
        break

    elif ord not in fruit:
        print("{}는(은) 목록에 없습니다.".format(ord))

    elif ord in fruit:
        t=fruit[ord] #이거 반대로 하면 큰일남,, value를 바꾸는게 되어버림

        if t>=1:
            fruit[ord]=t-1
            print("이제 {}는 {}개 남았습니다".format(ord,t-1))
            
        elif t==0:
            print("{}는(은) 품절입니다.".format(ord))
    
        