student_list=[3,7,8,0,1,0,4,11,9,0] #약속을 지키지 않을 때마다 30분씩 청소
c=[]
d=0
for a in student_list:
    b=a*30
    c.append(b)
for t in c:
    d=d+t


h=d//60
m=d%60
print(h,m)
print(c)
e=sum(c)
hour=e//60
min=e%60


print("{}시간 {}분".format(hour,min))

'''for st in student_list:
        tot_bun+=st*30'''