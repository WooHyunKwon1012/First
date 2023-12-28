# class Human:
#     def __init__(self,name,hobby,age):
#         self.name=name
#         self.hobby=hobby
#         self.age=age
#     def intro(self):
#         print("내이름은 %s. 나는 %s를(을) 좋아해"%(self.name,self.hobby))
#     def a(self):
#         print("나는 %s에 미쳤어"%self.hobby)

# person01=Human("터틀봇","그림그리기")
# person01.intro()
# person01.a()

class Woo:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def babo(self):
        print("{}는{}가{}아니야 바보야".format(self.a,self.b,self.c))
    def gogo(self):
        print("{}가{}거지{}바보야".format(self.b,self.a,self.c))

a=Woo("천재","학교","공부")
a.babo()
a.gogo()
