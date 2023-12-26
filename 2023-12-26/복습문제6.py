num1=int(input("김 밥 :"))
num2=int(input("떡볶이 :"))
num3=int(input("라면 :"))

price=3000*num1+3500*num2+2500*num3

ppl=int(input("같이 먹은 사람은 몇명입니까?:"))
price_per_people=price/ppl

print("지불하실 금액은 {}원입니다.".format(price))
print("지불하실 금액은 %d원입니다"%price)
print("지불하실 금액은 %s원입니다"%price)
print("지불하실 금액은"+str(price)+"원입니다")

print("{}원씩 배분하십시오".format(price_per_people))
