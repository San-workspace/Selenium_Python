
#class is user defeined prorto type or blue print
#contain method,object ,class varible
#multile function using inside the class are called methods

class calc():

    def __init__(self,a,b):
        self.a= a
        self.b= b

    def add(self):
        print('executing the add')
        return self.a+self.b
    def div(self):
        print('executing the div')
        return self.a / self.b

obj=calc(9,3) #syntax for creatingthe object
print(obj.add())
print(obj.div())


