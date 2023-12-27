dic01=dict(health=1,mana=5)
dic01['double']=8
print(dic01)

for t in dic01: #기본으로 키값을 가져옴
    print(t,'',end="♡ ")

print("\n")

for t in dic01.values(): #.values()가 값을 가져온다.
    print(t,'',end='※ ')

print("\n")
dic05=dict([('fine',2),('ine',5)])
print(dic05)
dic06=dict(yellow=3,red=2)
print(dic06)