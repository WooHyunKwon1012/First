
while True:
    t=int(input("횟수 입력 : "))
    a=t%2
    
    if a==0:
        b=t//2
        for y in range(1,b+1):
            h=y*2
            print(h)
        break

    if a==1:
        continue

num=int(input("입력:"))
for i in range(1,num+1):
    if i%2==1:
        continue
    print(i)