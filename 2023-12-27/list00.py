'''b=[] #b=list() 도 됨
for i in range(6):
    a=int(input("입력하세요:"))
    b.append(a) #자체로 더해주는 능력이 있어서 내가 따로 더하기 넣지 않아도 됨

bb = b.copy()
bb.sort() #sort는 그저 정렬해주는 것일뿐 다시 리스트를 주거나 하지는 않음, c=b.sort() 가 안됨
c=sorted(b)

print(b)
print(bb)
print(c)
print(b)'''

for t in range(5):
    print(t+1,end='') #end='' 는 print에 기본적으로 붙어있는 \n대신에 끝에 붙여주는 역할을 함
    a=int(input("메롱:"))
    
    