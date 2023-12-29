class bank:
    def __init__(self,won):
        self.won=won
    def get_balance(self):
        return self.won
    def plus(self,won):
        self.won+=won
        return self.won
    def minus(self,won):
        self.won-=won
        return self.won

a=bank(10000)
print(a.get_balance())
print(a.plus(4000))
print(a.minus(3000))
print(a.get_balance())