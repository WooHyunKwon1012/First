
# t=0
# while t<=99:
#     t=t+1
#     if t%3==0 and t%5==0:
#         print("FizzBuzz")
#     elif t%5==0:
#         print("Buzz")
#     elif t%3==0:
#         print("Fizz")
#     else:
#         print(t)

for t in range(1,101):
    if t%3==0 and t%5==0:
        print("FizzBuzz")
    elif t%5==0:
        print("Buzz")
    elif t%3==0:
        print("Fizz")
    else:
        print(t)