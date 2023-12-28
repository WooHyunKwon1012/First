from tkinter import*
main=Tk()
main.title("Tk")
main.geometry("300x200")

a=Label(main,text="안녕하세요",font="Arial 20")

a.pack()
ok_button=Button(main,text="확인",foreground="Red")
ok_button.pack()
cancel_button=Button(main,text="취소",foreground="Green")
cancel_button.pack()
img=PhotoImage(file="cat.png")
btn=Button(main,image=img)
btn.pack()
main.mainloop()