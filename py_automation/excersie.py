class calc():
    d=10  #class vrible
    def __init__(self,a,b,c): #instance var
        self.a=a
        self.b=b
        self.c=c
    def add(self):
        return self.a+self.b+self.c+calc.d #accessing cls and instance var

obj=calc(5,4,8)
print(obj.add())