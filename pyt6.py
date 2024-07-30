#Functions in Python, block of statements that perform a specific task.
#To avoid redundancy.(repetition) def(var1,var2...)

def adder(a,b,c):  #function defining
    sum = a+b+c #a,b,c are paramters
    print(sum)
    return sum
#Now do add three numbers we have to just call our function.
adder(3,5,6)   #function call

def add(a,b):
    return a+b
print(add(1,3))

def prin():
    i=1
    while i<=3:
        print("Hello")
        i+=1

print(prin())    

#If any function doesn't return anything then it will show None as output.
def prhello():
    print("Hello")

output = prhello()
print(output)

#Userr-defined functions:
#Print, it has end which is by default \n, if we manipulate it would show desired things.
print("aple", end=" ")
print("sarkar" , "parrot", end="$", sep="%")
print()

def product(a,b):
    print(a*b)

product(3,4)
#if here arguments are not given, it assumes by default a and b as given values., else it will show error.

def pro(a=1,b=3):
    print(a*b)

pro(2)
pro()
#Default values should be given from right side as, else it will throw error.
#pro(a=1,b) error

#Recursion in Python, when a function calls itself repeatedly.
def show(n):
    print(n)
    if(n>=2):
        show(n-1)

def show1(n):
    if(n==0):
        return
    print(n)
    show1(n-1)

show1(6)
show(6)

#recursion has base case like stop in range, where it terminates.

def show2(n):
    if(n==0):
        return
    print(n)
    show2(n-1)
    print("END")
#refer for explanation recusrsion apna college youtube
show2(3)
