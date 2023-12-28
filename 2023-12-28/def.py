def I(a):
    print(a,"그게 너야")

I("메롱")

def add_num(a,b):
    res=a+b
    print(res)
add_num(5,4)

def add_num(a,b):
    res1=a+b
    res2=a*b
    return res1,res2 #리턴을 넣어야 그 값을 다시 돌려줌
my_sum=add_num(4,5)
print(my_sum)
my_summ,my_mu=add_num(9,8)
print(my_summ,my_mu)