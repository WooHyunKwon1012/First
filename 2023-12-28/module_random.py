#랜덤 덧셈 계산
import random
R=0
while True:
    ran_1=random.randint(1,100)
    ran_2=random.randint(1,100)
    print("{}+{}=".format(ran_1,ran_2),end="")
    ans=int(input(""))
    if ans==ran_1+ran_2:
        print("정답입니다.")
        R=R+1
    elif ans!=ran_1+ran_2:
        print("오답입니다. 정답은 {}입니다\n{}개 맞추셨습니다.".format(ans,R))
        break
