def av3(a,b,c):
    t = (a+b+c)/3
    print(t)
    return av3

av3(2,3,7)

def ca1(a):
    print(len(a))

t=["sa","da","th"]
ca1(t)
#To print all items of list in a single line.
def ca2(a):
    for c in a:
        print(c, end=" ")

ca2(t)
print()#just for space
def facto(a):
    i=1
    j=1
    while i<=a:
        j*=i
        i+=1
    print(j)

facto(6)
        
def cuco(a):
    print("It is", a*70, "in Indian rupees.")

cuco(80)

def find(x):
    if(x%2==0):
        print("Even")
    else:
        print("Odd")

find(9)
find(8)
#Find factorial of n
def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1)*n

print(fact(6))
#To find sum of first n natural numbers, using recursion.
def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n

print(sum(10))

#To print all elements in a list using a recursive function.
list1 = ["Sarang", 2, 34, 45, 56]
def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

print_list(list1)
print_list(list1,1)
    