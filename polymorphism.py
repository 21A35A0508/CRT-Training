#mthod overloading-->runtime overloading--->takes latest
class A:
    def method_1(self,a,b):
        print("mul",a+b)
class B:
    def method_1(self,a,b):
        print("mul",a*b)
    def method_1(self,abc):
        print("value is",a*b)
obj=B()
obj.method_1(10)