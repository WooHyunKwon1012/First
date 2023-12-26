price=int(input("물건의 금액을 입력하세요 :"))
a="할인율"

# if price>=100000:
#     print("{} : 10%".format(a))
#     dis=int(price*0.1)
   
# elif 50000<= price< 100000:
#     print("{} : 7.5%".format(a))
#     dis=int(price*0.075)
  
# else:
#     print("{} : 5%".format(a))
#     dis=int(price*0.05)

# pay=price-dis
# print("구매가 : {} 원".format(price))
# print("할인 금액 : %d 원"%(dis))
# print("지불 금액 : {} 원".format(pay))

if price>=100000:
    dis=0.1
   
elif 50000<= price< 100000:
    
    dis=0.075
  
else:
    
    dis=0.05

dc_price=dis*price
pay=int(price-dc_price)
print("구매가 : {} 원".format(price))
print("할인 금액 : %d 원"%(dc_price))
print("지불 금액 : {} 원".format(pay))