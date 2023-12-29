import tkinter as tk
def click():
    print("클릭")
def clk():
    btn1.config(text="성공")


main=tk.Tk()
main.title("Click the button")
main.geometry("300x200")
lbl=tk.Label(main,text="클릭하세요",font="Arial 15")
lbl.pack()
btn=tk.Button(main,width=10,height=3,text="클릭",command=click)
btn.pack()
btn1=tk.Button(main,width=10,height=3,text="클릭",command=clk)
btn1.pack()
main.mainloop()