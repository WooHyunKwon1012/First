while True:
    a=int(input("숫자 입력 : "))
    output=1
    if 1<=a<=10:
        for input in range(1,a+1):
            output=input*output
        print("결과: {}".format(output))
        break
    else:
        print("잘못 입력하셨습니다. 다시 입력하십시오\n")
        continue

