#Object Oriented Programming:
#Class is a blueprint for creating objects.
#creating objects(instance)

class VI:
    name="Sarang"

s1 = VI()
s2 = VI()
print(s1.name)
print(s2.name)
#just like if blueprint of a car decides color of car as blue, similarly once name is written all objects in class will have same name.

class car:
    color = "blue"
    brand = "audi"

car1 = car()
print(car1.color)
print(car1.brand)

#Constructor: all classes have an init_() function, which is always executed
#when the class is being intiated.
class Student:
    college = "IIT Guwahati"
    def __init__(self,fullname,marks):  #init means intialization
        self.name = fullname      #wruting self is not mandatory but writing it is in trend.
        self.marks = marks
        self.college="IIT Kharagpur"
        print("adding..")

s1 = Student("Karan", 97)   #here this brackets calls the constructor.
print(s1.name)
print(s1.marks)
print(s1.name, s1.marks)
print(s1.college)
#Default constructors are those which are made by default by python, even if we don't make any.
#Parametrized constructors are those which are made by us. 
"""
Class and Instance Attributes
Class.attr which are common for any class
Obj.attr which are common for any object.
class attr are not written in constructor, whereas 
obj at is written as self.attr in constructor.
Obj attr is given priority than class atr

Methods are functions that belong to objects.

"""
class student:
    college_name="ABC"

    def __init__(self,name,marks):
        self.name =  name
        self.marks = marks

    def welcome(self):
        print("welcome student", self.name)

    def get(self):
        return self.marks

s1 = student("karan", 98)
s1.welcome()
print(s1.get())

#Static Methods: That don't use the self parameter.
#used where we have to work on class, where self makes no sense.

class st:
    @staticmethod #decorator: that allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.
    def college():
        print("IIT")

s1 = st()
print(s1)

#Abstraction: Hiding the implementation details of a class and only showing the essential features to the user
#like, if a car manufacturer don't show how his engine works, or a driver don't show to passenger how he use clutch and acc.

class motor:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    def start(self):
        self.clutch = True
        self.acc = True
        print("car started..")

mot1 = motor()
mot1.start()

#Encapsulation: Wrapping data and functions into a single unit(object)















