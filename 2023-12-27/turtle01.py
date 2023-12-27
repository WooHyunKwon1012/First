import turtle as t
t=t.Turtle()
t.shape("turtle")
a=int(input("숫자를 입력하시오:"))
L =360/a

if 3<=a<=9:
    for y in range(a):
        t.fd(50)
        t.left(L)
    input("press")

