marks=[50,49,70,100,65]
number=0
for mark in marks:
    number=number+1
    if mark>=60:
        print("{}번 학생은 합격입니다".format(number))
    else:
        print("%d번 학생은 불합격입니다"%number)

