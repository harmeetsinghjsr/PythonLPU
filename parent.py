'''class parent:
    def func1(self):
        print("this is in parent class")
class child(parent):
    def func2(self):
        print("this is in child class")
object=child()
object.func1()
object.func2()'''
class first:
    def func1(self):
        print("this is in first class")
class second:
    def func2(self):
        print("this is in second class")
class third(first,second):
    def func3(self):
        print("this is in third class")
object=third()
object.func1()
object.func2()
object.func3()



