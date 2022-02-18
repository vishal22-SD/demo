#class with class variable
class a:
  x = 5
ob=a()
print(ob.x)

#class constructor
class a:
  def __init__(self, name, marks):
    self.name = name
    self.marks = marks

p1 = a("John", 36)

print(p1.name)
print(p1.marks)

#object methods
class a:
  def __init__(self, name):
    self.name = name
  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = a("Tom")
p1.myfunc()

#singal inheritance
class a: #class name
    def func1(self): #create function
        print("This function is in parent class.")
# Derived class
class b(a):
    def func2(self):
        print("This function is in child class.")
object = b()
object.func1()
object.func2()

#multiple inheritance
class Class1:
  def m(self):
     print("In Class1")


class Class2(Class1):
    def m(self):
        print("In Class2")


class Class3(Class1):
    def m(self):
        print("In Class3")


class Class4(Class2, Class3):
    pass


obj = Class4()
obj.m()
