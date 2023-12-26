import turtle 
num=int(input("숫자를 입력하세요:"))

t1=turtle.Turtle()
turtle.pensize(10)

if num>=3 and num<8:
    
    t1.circle(50, steps=num)

else:
    t1.circle(50)
    

if num==3:

    print("삼각형")

if num==4:

    print("사각형")

if num==5:

    print("오각형")

if num==6:

    print("육각형")

if num==7:
    print("칠각형")
    
if num>=8:
    print("이제 거의 원이야")


numm=int(input("숫자를 입력하세요:"))



turtle.pensize(10)
if num>=3 and num<8:
    
    t1.circle(50, steps=numm)

else:
    t1.circle(50)
    
