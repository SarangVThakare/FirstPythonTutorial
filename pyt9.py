#del keyword is used to delete object properties or object itself.
class Student:
    def __init__(self,name):
        self.name = name

s1=Student("Sarang")
#del s1     (deletes object)
#del s1.name   (deletes attribute of that object)

"""Private(like) attributes and methods
Private attributes and methods are eant to be used only within the class and
not accessible from outside the class."""

class account:
    def __init__(self, acn, acp):
        self.acn = acn
        self.__acp = acp
    def reset(self):
        print(self.__acp)

acc1 = account("123", "I am password")
print(acc1.acn)
#By using two underscore in the front of an obj's attribute.
# print(__acc1.acp), writing this shows an error now.
#here as password may be case-sensitive,  it must not be disclosed outside.

acc1.reset()
#here the acp is printed as it was in the class.

class person:
    __name = "anonymous"
    def __hello(self):
        print("hello")

    def welcome(self):
        self.__hello()


p1 = person()

#print(p1.__name)  It shows error as now the method is private.
#print(p1.__hello())   It also shows error as its private.
#The need of such functions is internal and they are used inside class only.
#But here that hello can be called by tyhe weelcome function inside the class.
p1.welcome()

#Inheritance
#When one class(child/derived) derives the properties and methods of another class(parent/base).

class car:
    color = "any color"
    @staticmethod
    def start():
        print("start")

    @staticmethod
    def stop():
        print("stop")
    
class Bugati(car): #here we have written in brackets the name of that class whose properties are to be inherited.
    def __init__(self, name):
        self.name = name

car1 = Bugati("M30")
car2 = Bugati("S67")

car1.start()
car1.stop()
print(car1.color)
"""
Three types of inheritance:
Single inheritance, we derived one class from one parent class, as above eg.
Multi-level inheritance:
In it multiple generations are there.
Grandma-->Mother-->Daughter, now daughter inherited all properties of grandma and mother. 
"""

class M30(Bugati):
    def __init__(self, type):
        self.type = type
        
car3 = M30("kerosene")
car3.start()

#See here now the third level inherited and used property of two layers before.
"""Multiple inheritance
Derived class, can inherit properties from multiple classes.
"""
class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "welcome to class C"

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)

#Super Method, is used to access methods of the parent class.

# class jet:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("start")

#     @staticmethod
#     def stop():
#         print("stop")

# class rafel(jet):
#     def ___init__(self, name, type):
#         super().__init__(type)
#         self.name = name
#         super().start()

# jet1 = rafel("F37", "Vertical")
# print(jet1.type)
"""
Super method is used to se methods of diff parent classes in child class.

class Person:
    name = "anonymous"

    def changename(self,name):
        self.name = name
        
p2 = Person()
p2.changename("Shyam")
print(p2.name)          #Output: Shyam
print(Person.name)      #Output: anonymous
here due to object's name change class's name is not changed.
Now, if we have to change name
"""
#Method 1
class Person:
    name = "anonymous"

    def changename(self,name):
        Person.name = name
        
p2 = Person()
p2.changename("Shyam")
print(p2.name)         
print(Person.name) 

#Method 2
class Person1:
    name = "anonymous"

    def changename(self,name):
        self.__class__.name ="shyam"
        
p2 = Person1()
p2.changename("Shyam")
print(p2.name)         
print(Person1.name) 

"""
Class method,
a class method is bound to the class and receives the class as an implicit first argument.
note - static method can't access or modify class state and generally for utility
"""
class Person2:
    name="anonymous"   
    @classmethod        #decorator
    def changename(cls, name):
        cls.name = name

p3 = Person2()
p3.changename("Shyam")
print(p3.name)         
print(Person2.name) 

#Property, @property decorator on any method in the class to use the method as a property.
#E.g.  if a teacher inputs wrong marks of a student and then goes to change it as 
#percentage is calculated first, it would not change his percentage.

# class jee:
#     def __init__(self,phy,chem,math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         self.percentage = str((self.phy + self.math + self.chem)/3) + "%"

# st1 = jee(98,97,95)
# print(st1.percentage)
# st1.phy=86
# print(st1.phy)
#Method 1: Create a function to recalculate it.
class jee:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.math + self.chem)/3) + "%"
    def cal(self):
        self.percentage = str((self.phy + self.math + self.chem)/3) + "%"
st1 = jee(98,97,95)
print(st1.percentage)
st1.phy=86
print(st1.phy)
st1.cal()
print(st1.percentage)

#Method 2: This converts function to property, leading to calculation with updated data.

class neet:
    def __init__(self,phy,chem,bio):
        self.phy = phy
        self.chem = chem
        self.bio = bio
        
    @property
    def percentage(self):
        return str((self.phy + self.bio + self.chem)/3) + "%"
st2 = neet(98,97,95)
print(st2.percentage)
st2.phy=86
print(st2.phy)
print(st2.percentage)

#Polymorphism: Operator Overloading
print(1+2)
print("1"+"2")
print([1]+[2])
#+ is a operator whose function changes according to data type.
#As it is written in python, its implicit overloading.

class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, "i +", self.y, "j")

    def __add__(self, vec):
        newx = self.x + vec.x
        newy = self.y + vec.y
        return vector(newx,newy)
    
v1 = vector(1,3)
v1.show()
v2 = vector(2,8)
v2.show()
# v3 = v1.add(v2)
# v3.show()   
#To be used if dunder function is not used.
v3 = v1+v2
v3.show()
#We do operator overloading for our classes, using Dunder functions(with both side __)











