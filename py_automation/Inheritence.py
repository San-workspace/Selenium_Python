#inheritence :
#inheritence is nothing but acquring the properteis ,definition from parent to child class
from cls_constructor import calc

class inher(calc):
      num2=100
      def __init__(self):
          calc.__init__(self,3,2)

      def inhercheck(self):
          return self.add()+ self.num2

obj=inher()
print(obj.inhercheck())