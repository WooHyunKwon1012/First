money=3000
juice=10

while money:
    print("음료가격: 300원")
    juice=juice-1
    money=money-300
    print("남은 돈 : "+"{}".format(money)+"원")
    print("남은 쥬스는 %d개 입니다\n"%juice)
    if juice ==0:
        print("쥬스가 없습니다.")
        break


