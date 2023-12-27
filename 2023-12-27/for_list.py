text=['one','two','three']

for i in text:
    print(i)

num=[(1,2,3),(4,5,9),(4,3,2)]
for (a,b,c) in num:
    print("합 : {}\n리스트 : {}".format(a+b+c,(a,b,c)))