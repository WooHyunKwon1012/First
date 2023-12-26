# a=''
# t=len(a)
# while t<=25:
#      b = input("입력  : ") 
#      a = a + b
#      t = len(a)
    

#      if t>25:
#         break
#      else: 
#         print("출력 : "+"{} ({})".format(a,t))


'''    
input_str=''
output_str=''

while True:
    in_str=input("입력 : ")
    out_str=in_str+out_str
    if len(out_str>=25):
        break
    print('출력 : {}({})".format(out_str,len(out_str)))
'''

a=''

while len(a)<=25:
    b=input("입력 : ")
    a=a+b
    if len(a)>25:
        break
    print("{}({})".format(a,len(a)))

