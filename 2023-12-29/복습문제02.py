class grade:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def get_score(self):
        print(self.a+self.b+self.c)

Mike=grade(30,40,50)
Mike.get_score()
