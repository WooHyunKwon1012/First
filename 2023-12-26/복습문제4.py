num1=int(input("점수를 입력하시오: "))
num2=int(input("점수를 입력하시오: "))

if num1 >=80 and num2>=80:
    print("합격")

else:
    print("불합격")

if num1 >=80:
    
    if num2>=80:
        print("합격")
    else: print("불합격")
    
else:
    print("불합격")