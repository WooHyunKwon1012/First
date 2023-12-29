from tkinter import*
def addNum():
    n1=int(ent1.get())
    n2=int(ent2.get())
    lbAns.config(text=n1+n2)  #내용을 업데이트 할때 config를 쓴다
def divNum():
    n1=int(ent1.get())
    n2=int(ent2.get())
    lbAns.config(text=n1/n2)
def subNum():
    n1=int(ent1.get())
    n2=int(ent2.get())
    lbAns.config(text=n1-n2)
def mulNum():
    n1=int(ent1.get())
    n2=int(ent2.get())
    lbAns.config(text=n1*n2)
main=Tk()
main.title("my calc")
main.geometry("400x300")

lb=Label(main)
lb['text']='숫자 2개를 입력하세요'
lb.pack()

ent1=Entry(main)
ent1.pack()
ent2=Entry(main)
ent2.pack()

a=Label(main)
a.pack()

btnAdd=Button(main,text="더하기",command=addNum)
btnAdd.pack()
btnsub=Button(main,text="빼기",command=subNum)
btnsub.pack()
btnmul=Button(main,text="곱하기",command=mulNum)
btnmul.pack()
btndiv=Button(main,text="나누기",command=divNum)
btndiv.pack()

lbAns=Label(main,foreground="Red")
lbAns.pack()
a=Label(main,text="\n")
a.pack()


main.mainloop()