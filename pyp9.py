"""Define a circle class to create a circle r using the constructor.
Define an Area() Method of the class which calculates the area of the circle.
Define a Perimeter() Method of the class which allows you to calculate the perimeter of the circle.
"""
class circle:
    def __init__(self, r):
        self.r = r
    def show(self):
        print(self.r)
    def area(self):
        print(int(self.r)*int(self.r)*3.14)
    def peri(self):
        return 6.28*int(self.r)

c1 = circle("4")
c1.show()
c1.area()
print(c1.peri())

class Employee:
    def __init__(self, role, dept, sal):
        self.role = role
        self.dept = dept
        self.sal= sal
    def showDetails(self):
        return(self.role,self.dept, self.sal)
    
e1 = Employee("Engineer", "CS", "1Cr")
print(e1.showDetails())

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super() .__init__("Engineer", "Data Science", "1Cr")

    def showID(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Profession: ", self.role)
        print("Department: ", self.dept)
        print("Salary: ", self.sal)

e2 = Engineer("Sarang", 17)
e2.showID()

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    
    def __gt__(self ,od2):
        return self.price > od2.price
       
           # print("price of order 1> price of ord")

ord1 = Order("chips", 20)
ord2 = Order("tea", 10)
print(ord1>ord2)







