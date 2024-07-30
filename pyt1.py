print("Sarang")
print('Sarag')
print('''Saran''')
print(" Thakare")
#print(""""") print(""") not allowed
print("Sarang",     "Thakare")
#any no of spaces is allowed in this 
#print is a function used to get output

print(2)
""" rules for identifiers
#can be uppercase, lowercase, digits, underscore
#can't start with digit 1var not allowed var1 allowed
#don't use special symbols, length is limitless but use simple, short and meaningful names.
"""
name = "sarang"
age=-17
price=     10.0
#you may leave space or not in giving var
print(type(name))
print(type(age))
print(type(price))

#data types
#integers, string , float(decimal), boolean, none
a = True
b = None
print(type(a))
print(type(b))
#Keywords reserved to python
#and, as, assert, break, class, continue, def, del, elif, else, except, finally, False, 
#for, from, global, if, import, in, is, lambda, nonfocal, None, not, or, pass, raise, return,
# True, try, with, while,yield
#python is case-sensitive, whereas mssql is not case-sensitive

c = 3
d = 2
sum1 = c + d
diff1 = c-d
product = c*d
div1 = c/d
print(sum1)
print(diff1)
print(product)
print(div1)
print(c+d)
"""Types of Operators
a + b , a is operands and + is operator
Arithmetic Operator(+,-,*,/,%,**)
Relational,/Comparison Operrators(==, !=, >,<,>=,<=)
Assignment Operators
Logical Operators
"""
#Aritmetic O.
l=5
m=3
n=6
print(l+m)
print(l-m)
print(l*m)
print(l/m)
print(n/m)
"""division always gives output in float type
%its modulo operator and used to find remainder
** its power operator and used to find power of something(l**m)<=>l's power m
"""
print(l%m)
print(m%l)
print(l**m)
"""in python equal to is not written as = instead == and not equal to as !=
in python relational operators always give output as boolean
"""
g=4
h=5
m=4
print(g==h)
print(g == h)
print(g != m)
print(h >= g)
print(h > g)
print(m<=g)
print(g<h)

#Assignment Operator(=, +=, -=, *=,/=, %=, **=)

a1 = 2
a1= a1 + 10
a2 = a1 +3
print(a1)
print(a2)
a1 += 10
a1 -= 100
print("my no:", a1)
a1 /= 13
print("my no:", a1)
a1 **= 2
print("my no:", a1)
a1 %= 7
print("my no:", a1)
a1 *= 2
print("my no:", a1)
"""Logical Operators (not,and,or)
"""
f1=20
f2=30
print(not True)
print(not f1>f2)
print(not (f1>f2))
ans1 = True
ans2 = False
ans3= False
ans4=True
print("answers:", ans1 and ans2)
print("answers:", ans1 and ans4)
print("answers:", ans3 and ans2)
print("Space")
print("answers:", ans1 or ans2)
print("answers:", ans1 or ans4)
print("answers:", ans3 or ans2)

x=4
b5=16
y=4
print((x==y) and (x!=b5))
print((x==y) or (x!=b5))
print(not y==x)
print(not (y==x))
"""Type Conversion of Types
Automatic Conversion and Type Casting
In automatic conversion it may add str and float values, it converts int to float which seems to be more superior than int
whereas it would n't add str to int or float even only a no is present in it
then we have to manually convert it into diff types"""
p1=2
p2=3.0
p3="5"
print(p1+p2)
print(p1==p2)
#To convert float to str
p2 = int(p2) # not merely int(p2)
p3 = float(p3)
p4= int(4.00)
print(type(p2))
print(p3)
print(p4)
p4= str(p4)
print(p4, "now I am a string")

#INPUT 
# wrong as space is not present after what's written, name11= input("First Name:")
name11= input("First Name:" )
print("You are very near,",name11)
age17=input("age" )
print(type(age17))
#in python simple input always take the data as str, if we have to cast it into diff format we have to use type casting

age15=int(input("age" ))
print(type(age15))