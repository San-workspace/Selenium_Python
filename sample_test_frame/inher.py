

from Trial.calc import calc



class inher(calc):
    def __init__(self,c):
        self.c = c
        calc.__init__(6,7)

    def mul(self):
        return self.a * self.c

    def div(self):
        return self.b / self.a


obj1 = inher(5)
print(obj1.add())
print(obj1.div())
