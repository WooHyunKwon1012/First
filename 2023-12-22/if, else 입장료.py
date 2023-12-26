age=int(input("나이:"))

if age<=7 or age>=65:
    print("무료입니다!")
elif 8<=age<=18:
    print("1500원입니다")
else:
    print("3000원입니다")
