# import random as r #로또 생성기(6개 숫자, 1~45)
# Lotto=list(range(1,46))
# Week=r.sample(Lotto,6) #한번에 6개를 가져오는 것
# print(Week)

import random as r 
Lotto_1=[]
while len(Lotto_1)<=5:
    R=r.randint(1,45)
    if R in Lotto_1:
        continue
    else:
        Lotto_1.append(R)
Lotto_1.sort()
print(Lotto_1)



    