num1=int(input("점수를 입력하시오: "))
num2=int(input("점수를 입력하시오: "))
num3=int(input("점수를 입력하시오: "))

if num1 >=90 or num2>=90 or num3>=90:
    print("합격")

else:
    print("불합격")


if num1<90:
    if num2<90:
        if num3<90:
            print("불합격")
        
        else: print("합격")
    else: print("합격")

else:
    print("합격")

if num1<90:
    if num2<90:
        if num3<90:
            print("불합격")

else:
    print("합격")

