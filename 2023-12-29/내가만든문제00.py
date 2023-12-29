class Woo:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def who(self):
        print(f"{self.a}는 천재당")

a=Woo("WooHyunKwon",2,3)
a.who()
