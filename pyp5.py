#To print even numbers
for i in range(1,51,2):
    print(i)
#To print nos from 0 to 100
for c in range(1,101):
    print(c)    
#To print nos from 100 to 1
for c in range(100,0,-1):
    print(c)
#To print the multiplication table of a number.
#method-1
a = int(input("Enter a number: ", ))
b = a*11
for c in range(a,b,a):
    print(c)
#method-2
for ch in range(1,11):
    print(ch*a)

num1 = int(input("Enter a number:", ))
mor = 1
num2 = 0
while mor<=num1:
    num2+=mor
    mor+=1
print(num2)

w1 = int(input("Find factorial of:", ))

u = 1
for c in range(1,w1+1):
    u*=c
print("Answer: ", u)

    