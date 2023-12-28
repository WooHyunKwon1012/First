def fun1():
    var="전역변수"
    print(var)

def fun2():
    global var
    var="글로벌변수"
    print(var)

var="전역변수"
print(var)
fun1()
fun2()
var="전역변수수정"
print(var)
fun1()
fun2()