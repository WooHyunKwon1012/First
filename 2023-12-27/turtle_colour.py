import turtle as t 

color=['red','yellow','blue','black','green','pink']
while  True:
    num=int(input("Write number : "))
    if 3<=num<=9:
        t=t.Turtle() 
        t.shape("turtle")
        while True:
            c=input("Write color : ")
            if c in color:
                t.color(c)
                t.begin_fill()
                for i in range(num):
                    t.fd(100)
                    t.left(360/num)
                t.end_fill()
                input("press")
                break
            else: print("색상을 다시 입력하세요")
            continue
        
    else: 
        print("숫자를 다시 입력하세요")
        continue

# import turtle as t 

# color=['red','yellow','blue','black','green','pink']
# while  True:
#     c=input("Write color : ")
#     if c in color:
#         t=t.Turtle() 
#         t.shape("turtle")
#         while True:
#             num=int(input("Write number : "))
#             if 3<=num<=9:
#                 t.color(c)
#                 t.begin_fill()
#                 for i in range(num):
#                     t.fd(100)
#                     t.left(360/num)
#                 t.end_fill()
#                 input("press")
#                 break
#             else: print("숫자를 다시 입력하세요")
#             continue
        
#     else: 
#         print("색상을 다시 입력하세요")
#         continue

