import random as r
from tkinter import*

main=Tk()
main.title("my calc")
main.geometry("400x300")
a=r.randrange(1,10)
b=r.randrange(1,10)
p=r.choice(["+","x","-","/"])

if p=="+":
    d=a+b
if p=="-":
    d=a-b
if p=="/":
    d=a/b
if p=="x":
    d=a*b

lb=Label(main,text="{}{}{}=?".format(a,p,b))
lb.pack()

ent1=Entry(main)
ent1.pack()


def right():
    c=float(ent1.get())
    if d==c:
        p=Label(main,text="정답입니다")
        p.pack()
    else:
        p=Label(main,text="오답입니다.정답은 {}입니다".format(d))
        p.pack()

check=Button(main,text="확인",command=right)
check.pack()
p=Label(main)
p.pack()


main.mainloop()